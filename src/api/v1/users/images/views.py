from os import path

from app import images as localImage
from flask import abort, jsonify, make_response, request
from flask_jwt_extended import current_user, jwt_required
from flask_restx import Resource, fields
from src.api.v1.users.images.model import Image, ImageForm, ImagePermission
from src.api.v1.users.images.service import *
from src.api.v1.users.views import ns_users
from src.utils import flatten, getRandomFileName
from werkzeug.datastructures import CombinedMultiDict
from werkzeug.utils import secure_filename


@ns_users.route("/<string:userId>/images")
class ListAndUploadImage(Resource):
    @jwt_required()
    def get(self, userId):
        # current_user is User document returned from user_lookup_loader
        curUserId = str(current_user.id)

        if userId != curUserId:
            abort(401, description="User is not authorized")

        images = getAllImages(curUserId)
        if images:
            imageList = [(img.nameImg + img.extImg) for img in images]
            return make_response(
                jsonify(imageList),
                200,
            )

        return make_response(
            jsonify([]),
            200,
        )

    @jwt_required()
    def post(self, userId):
        curUserId = str(current_user.id)

        if userId != curUserId:
            abort(401, description="User is not authorized")

        # Because we pass file via files request, not from body
        form = ImageForm(CombinedMultiDict((request.files, request.form)))

        if form.validate_on_submit():
            data = request.form
            quotient = data["quotient"]

            file = form.imageFile.data
            filename = secure_filename(file.filename)

            fileSplitName, ext = path.splitext(filename)

            # Query to check duplicate file name
            imageList = getOneImage(curUserId, fileSplitName)

            if imageList:
                fileSplitName = getRandomFileName(fileSplitName)

            image = Image(
                userId=userId,
                nameImg=fileSplitName,
                dataImg=file,
                quotientImg=quotient,
                extImg=ext,
            )
            # Save locally
            localImage.save(request.files["imageFile"])
            # Save on Mongo
            image.save()
            return make_response(
                {
                    "img_name": image.nameImg + image.extImg,
                },
                200,
            )

        if form.errors:
            errorMessage = ", ".join(flatten(form.errors))
            abort(422, description=errorMessage)


@ns_users.route("/<string:userId>/images/<string:fileName>")
class DownloadAndDeleteImage(Resource):
    @jwt_required()
    def get(self, userId, fileName):
        curUserId = str(current_user.id)

        image = getOneImage(userId, fileName)

        if image:
            imagePermit = getOneImagePermission(userId, fileName, curUserId)

            # XOR ?
            if (not imagePermit) == (userId != curUserId):
                abort(401, description="User is not authorized")

            data_byte = image.dataImg.read().decode("ISO-8859-1")
            return make_response(
                {
                    "img_name": image.nameImg + image.extImg,
                    "img_content": data_byte,
                    "quotient": image.quotientImg,
                },
                200,
            )

        abort(404, description="Image not found")

    @jwt_required()
    def delete(self, userId, fileName):
        curUserId = str(current_user.id)

        if userId != curUserId:
            abort(401, description="User is not authorized")

        # fileExt = getExtension(request)
        image = getOneImage(curUserId, fileName)

        if image:
            image.delete()
            return make_response("", 204)

        abort(404, description="Image not found")


@ns_users.route("/<string:userId>/images/download-all")
class DownloadImageAll(Resource):
    @jwt_required()
    def get(self, userId):
        curUserId = str(current_user.id)

        if userId != curUserId:
            abort(401, description="User is not authorized")

        images = getAllImages(curUserId)

        if images:
            data = []
            for image in images:
                data_byte = image.dataImg.read().decode("ISO-8859-1")
                content = {
                    "img_name": image.nameImg + image.extImg,
                    "img_content": data_byte,
                    "quotient": image.quotientImg,
                }
                data.append(content)

            return make_response(
                jsonify([*data]),
                200,
            )

        # Because images can be None if there is no image on database, so instead of
        # return an error, we return an empty array
        return make_response(
            jsonify([]),
            200,
        )


@ns_users.route(
    "/<string:userId>/images/<string:fileName>/permissions/<string:userPermissionId>"
)
class EditImagePermission(Resource):
    @jwt_required()
    def get(self, userId, fileName, userPermissionId):
        curUserId = str(current_user.id)

        if userId != curUserId:
            abort(401, description="User is not authorized")

        imageOnePermit = getOneImagePermission(userId, fileName, userPermissionId)

        if not imageOnePermit:
            abort(404, description="Permission for User id not found")

        return make_response(
            jsonify(imageOnePermit),
            200,
        )

    @jwt_required()
    def put(self, userId, fileName, userPermissionId):
        curUserId = str(current_user.id)

        if userId != curUserId:
            abort(401, description="User is not authorized")

        imageOnePermit = getOneImagePermission(userId, fileName, userPermissionId)

        if not imageOnePermit:
            abort(404, description="Permission for User id not found")

        image = getOneImage(curUserId, fileName)
        if not image:
            abort(404, description="Image not found")

        sharedUserRole = request.form["role"]
        editOneImageRolePermission(userId, fileName, userPermissionId, sharedUserRole)
        image.reload()
        return make_response("", 204)

    @jwt_required()
    def delete(self, userId, fileName, userPermissionId):
        curUserId = str(current_user.id)

        if userId != curUserId:
            abort(401, description="User is not authorized")

        imageOnePermit = getOneImagePermission(userId, fileName, userPermissionId)

        if not imageOnePermit:
            abort(404, description="Permission for User id not found")

        image = getOneImage(curUserId, fileName)
        if not image:
            abort(404, description="Image not found")

        deleteOneImagePermission(userId, fileName, userPermissionId)
        # image.permissions.pop(index)
        image.reload()
        return make_response("", 204)


@ns_users.route("/<string:userId>/images/<string:fileName>/permissions")
class ShareImage(Resource):
    @jwt_required()
    def get(self, userId, fileName):
        curUserId = str(current_user.id)

        if userId != curUserId:
            abort(401, description="User is not authorized")

        image = getOneImage(curUserId, fileName)
        if not image:
            abort(404, description="Image not found")

        return make_response(
            jsonify(image.permissions),
            200,
        )

    @jwt_required()
    def post(self, userId, fileName):
        curUserId = str(current_user.id)

        if userId != curUserId:
            abort(401, description="User is not authorized")

        image = getOneImage(curUserId, fileName)
        if not image:
            abort(404, description="Image not found")

        sharedUserId = request.form["user_id"]
        sharedUserRole = request.form["role"]
        imageOnePermit = getOneImagePermission(userId, fileName, sharedUserId)
        # DB can find a permission has userId == curUserId
        if imageOnePermit:
            abort(409, description="Permission user id is already exists")

        newPermission = ImagePermission(userId=sharedUserId, role=sharedUserRole)
        image.permissions.append(newPermission)
        image.save()
        return make_response("", 201)
