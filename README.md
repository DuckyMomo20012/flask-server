<div align="center">

  <h1>Image-N-crypt</h1>

  <p>
    Flask server for storing encrypted images
  </p>

<!-- Badges -->
<p>
  <a href="https://github.com/DuckyMomo20012/image-n-crypt/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/DuckyMomo20012/image-n-crypt" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/DuckyMomo20012/image-n-crypt" alt="last update" />
  </a>
  <a href="https://github.com/DuckyMomo20012/image-n-crypt/network/members">
    <img src="https://img.shields.io/github/forks/DuckyMomo20012/image-n-crypt" alt="forks" />
  </a>
  <a href="https://github.com/DuckyMomo20012/image-n-crypt/stargazers">
    <img src="https://img.shields.io/github/stars/DuckyMomo20012/image-n-crypt" alt="stars" />
  </a>
  <a href="https://github.com/DuckyMomo20012/image-n-crypt/issues/">
    <img src="https://img.shields.io/github/issues/DuckyMomo20012/image-n-crypt" alt="open issues" />
  </a>
  <a href="https://github.com/DuckyMomo20012/image-n-crypt/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/DuckyMomo20012/image-n-crypt.svg" alt="license" />
  </a>
</p>

<h4>
    <a href="https://github.com/DuckyMomo20012/image-n-crypt/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/DuckyMomo20012/image-n-crypt">Documentation</a>
  <span> · </span>
    <a href="https://github.com/DuckyMomo20012/image-n-crypt/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/DuckyMomo20012/image-n-crypt/issues/">Request Feature</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->

# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
  - [Screenshots](#camera-screenshots)
  - [Tech Stack](#space_invader-tech-stack)
  - [Features](#dart-features)
  - [Environment Variables](#key-environment-variables)
- [Getting Started](#toolbox-getting-started)
  - [Prerequisites](#bangbang-prerequisites)
  - [Installation](#gear-installation)
  - [Running Tests](#test_tube-running-tests)
  - [Run Locally](#running-run-locally)
  <!-- - [Deployment](#triangular_flag_on_post-deployment) -->
- [Usage](#eyes-usage)
- [REST API Documentation](#book-rest-api-documentation)
- [RSA Encryption Algorithm](#crystalball-rsa-encryption-algorithm)
- [Roadmap](#compass-roadmap)
- [Contributing](#wave-contributing)
  - [Code of Conduct](#scroll-code-of-conduct)
- [FAQ](#grey_question-faq)
- [License](#warning-license)
- [Contact](#handshake-contact)
- [Acknowledgements](#gem-acknowledgements)

<!-- About the Project -->

## :star2: About the Project

<!-- Screenshots -->

### :camera: Screenshots

<div align="center">
  <img src="https://user-images.githubusercontent.com/64480713/177001704-d6ca292f-02e3-41f5-97e4-8ff6064e0fa1.png" alt="screenshot" />
</div>

<!-- TechStack -->

### :space_invader: Tech Stack

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
  </ul>
</details>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://flask.palletsprojects.com/en/latest/">Flask</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.mongodb.com/">MongoDB</a></li>
  </ul>
</details>

<details>
<summary>DevOps</summary>
  <ul>
    <li><a href="https://www.docker.com/">Docker</a></li>
    <li><a href="https://www.jenkins.io/">Jenkins</a></li>
  </ul>
</details>

<!-- Features -->

### :dart: Features

- Registration.
- Login.
- Storing image: app client encrypts the image with RSA and sends the request to
  the server to store the image.
  - Image encrypted is required to be **openable** and can't be recognized by attackers.
- View the image list.
- Download image: client download encrypted images and decrypts it using the
  user's RSA private key.
  - Download one image.
  - Download all images.
- Share the image with others: other users can download the image.
- After registration, an account is created with this information:
  - username.
  - ID.
  - RSA public key (provided by the client app for the user after registration).
- Server connects with the client by using REST API.

<!-- Env Variables -->

### :key: Environment Variables

To run this project, you will need to add the following environment variables to
your .env file

**App configs**

`SECRET_KEY`: Secret key for Flask application

`SESSION_COOKIE_SECURE`: Controls whether the cookie should be set with the
HTTPS protocol. Default: `False`.

`UPLOADED_IMAGES_DEST`: Destination folder for server downloading uploaded
images.

`WTF_CSRF_ENABLED`: Controls whether CSRF protection is enabled. Default:
`False` (Recommend).

`FLASK_ENV`: Enable hot reloading in `development` mode. Default: `production`.

> NOTE: Change to "development" to enable hot reloading.

**JWT configs**

`JWT_ACCESS_TOKEN_EXPIRES`: Time in seconds for access token expiration.
Default: `3600` (1 hour).

`JWT_SECRET_KEY`: Secret key for JWT.

**MongoDB configs**

`MONGODB_HOST`: An URI to connect to your database

E.g:

```
# App configs
SECRET_KEY="my secret key"
SESSION_COOKIE_SECURE=False
UPLOADED_IMAGES_DEST="src/assets"
WTF_CSRF_ENABLED=False
# Change to "development" to enable hot reloading
FLASK_ENV="production"

# JWT configs
JWT_ACCESS_TOKEN_EXPIRES=3600 # 1 hour
JWT_SECRET_KEY="my super secret key"

# MongoDB configs
# HOST not URI
MONGODB_HOST="mongodb+srv://{username}:{password}@crypto-image.u1r0p.mongodb.net/test"
```

You can also checkout file `.env.example` to see all required environment
variables.

<!-- Getting Started -->

## :toolbox: Getting Started

<!-- Prerequisites -->

### :bangbang: Prerequisites

This project uses [Poetry](https://python-poetry.org/) as package manager

Linux, macOS, Windows (WSL)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Read more about installation on
[Poetry documentation](https://python-poetry.org/docs/master/#installation).

<!-- Installation -->

### :gear: Installation

Install image-n-crypt with Poetry

```bash
poetry install
cd image-n-crypt
```

<!-- Running Tests -->

### :test_tube: Running Tests

- **Test REST API endpoints**: You can test endpoints using these ways:

  - [Hoppscoth](https://hoppscotch.io/): an open-source API development
    ecosystem

    ![hoppscotch.io](https://user-images.githubusercontent.com/64480713/177003377-aa1b901e-fa47-474d-bbdf-3d287192f915.png)

    - You can import pre-defined REST API endpoints from the file
      `data/hoppscoth.json` to Hoppscotch.

  - **Local Swagger documentation**: a Swagger UI is generated from REST API
    endpoints using Flask-RESTX.

    ![swagger](https://user-images.githubusercontent.com/64480713/177001704-d6ca292f-02e3-41f5-97e4-8ff6064e0fa1.png)

    - You can access this documentation: **http://127.0.0.1:5000/api/v1/**

  - **File `client/api.py`**: pre-defined functions to send requests to the
    server.

  - **Client console (Not recommended)**: poorly crafted client.

    - You can run this client using the file `client/main.py`.

    > NOTE: But you can use this client to **decrypt** downloaded images!.

- **Sample data**:

  - You can import sample data from folder `data` to your database.

  - Test data will have these sample users:

    <details>
    <summary>Sample users</summary>

    ```
    admin:
        password: admin
        private key: rsa_admin.txt
    admin2:
        password: admin
        private key: rsa_admin2.txt
    admin2:
        password: admin
        private key: rsa_admin3.txt
    ```

    </details>

<!-- Run Locally -->

### :running: Run Locally

Clone the project

```bash
git clone https://github.com/DuckyMomo20012/image-n-crypt.git
```

Go to the project directory

```bash
cd image-n-crypt
```

Install dependencies

```bash
poetry install
```

Activate virtual environment

```bash
poetry shell
```

Start the program

```bash
poe dev
```

OR

```bash
flask run
```

Access local Swagger documentation

http://127.0.0.1:5000/api/v1/

<!-- Deployment -->

<!-- ### :triangular_flag_on_post: Deployment

To deploy this project run

```bash
  yarn deploy
``` -->

<!-- Usage -->

## :eyes: Usage

First, you need to register an account.

To register an account, you need to generate RSA key pair. You have to use the
function `generateAndWriteKeyToFile` in `src.helpers.crypto.crypto.py` to
generate key pair.

This will create two files:

- `rsa.txt`: RSA private key (This file must be kept secretly).
- `rsa_pub.txt`: RSA public key.

OR:

- Using `register` from `client/api.py`.
- Using client console.

Then you can log in using your newly created account.

After login, you will receive an `access_token`.

<details>
<summary>Screenshot</summary>

![login response](https://user-images.githubusercontent.com/64480713/177004501-ea468252-6b12-47fa-9df7-c45824055cc9.png)

</details>

Use `access_token` to access protected endpoints:

- **Hoppscotch**:

  You have to paste your access token in the `Authorization` tab for each
  request. E.g:

  <details>
  <summary>Screenshot</summary>

  ![hoppscotch token example](https://user-images.githubusercontent.com/64480713/177004894-18f9093d-5748-4b1c-a7cc-3508e0a7cf19.png)

  </details>

  > NOTE: You have to choose **Authorization Type**: `Bearer`

- **Swagger doc**: you MUST add your access token to access protected
  endpoints. By clicking the `Authorize` button:

  <details>
  <summary>Screenshot</summary>

  ![authorize button](https://user-images.githubusercontent.com/64480713/177004457-8a6768f8-9119-40d5-a82e-6e58d5a78d99.png)

  </details>

  OR: clicking the **lock icon (:lock:)** on protected endpoints.

  Then type your access token in the input field. E.g:

  ```
  Bearer eyJ0eXAiO...
  ```

  > NOTE: Must be in the format `Bearer {access_token}`.

- **File `client/api.py`**:

  You have to call both functions `login` and `getUserInformation`:

  <details>
  <summary>Example code</summary>

  ```python
  login(username="admin", password="admin")
  getUserInformation()
  ```

  </details>

> NOTE: Access token will be expired after 1 hour.

<!-- REST API Documentation -->

## :book: REST API Documentation

You can use local Swagger documentation to see details about endpoints.

OR:

See it on [Wiki](https://github.com/DuckyMomo20012/image-n-crypt/wiki), [REST API
endpoints](https://github.com/DuckyMomo20012/image-n-crypt/wiki/REST-API-endpoints)
page.

<!-- RSA Encryption Algorithm -->

## :crystal_ball: RSA Encryption Algorithm:

This section has moved to
[Wiki](https://github.com/DuckyMomo20012/image-n-crypt/wiki), [RSA encryption algorithm](https://github.com/DuckyMomo20012/image-n-crypt/wiki/RSA-encryption-algorithm) page.

<!-- Roadmap -->

## :compass: Roadmap

- [x] Important: Remove entirely CSRF protection. ~~Keeps CSRF for
      Authentication~~
- [x] Set the expiration time for the token. NOTE: It works!.
- [x] Add validator for only .PNG image file.
- [ ] Allow user to get back revoked token.
- [ ] Handle expired token error.
- [ ] Support more image extensions, and more file types.
- [ ] Client support decrypt image service.
- [ ] Handle file permissions (read/write)

<!-- Contributing -->

## :wave: Contributing

<a href="https://github.com/DuckyMomo20012/image-n-crypt/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=DuckyMomo20012/image-n-crypt" />
</a>

Contributions are always welcome!

<!-- Code of Conduct -->

### :scroll: Code of Conduct

Please read the [Code of Conduct](https://github.com/DuckyMomo20012/image-n-crypt/blob/main/CODE_OF_CONDUCT.md)

<!-- FAQ -->

## :grey_question: FAQ

- Is this project still maintained?

  - Yes, but we will only update UI, docs, or dependencies. New features won't
    be added frequently.

- Is this project ready for production?

  - No, this is a small project for practicing cryptographic systems or schemes.
    This wasn't meant for production.
  - RSA algorithm is **implemented from scratch**, which is **unsafe** for
    production.

- Client console error: `ModuleNotFoundError: No module named 'src'`:

  - You are not exporting PYTHONPATH to the project directory.

  - Run this command:

    - Windows:

      ```console
      set PYTHONPATH=%cd%
      ```

    - Linux:

      ```bash
      export PYTHONPATH=$(pwd)
      ```

- Decrypt image took too long:

  - Because we implement the RSA algorithm from scratch, so it is unsafe and has
    slow performance. You should upload an image with a smaller size.

<!-- License -->

## :warning: License

Distributed under MIT license. See [LICENSE](https://github.com/DuckyMomo20012/image-n-crypt/blob/main/LICENSE) for more information.

<!-- Contact -->

## :handshake: Contact

Duong Vinh - [@duckymomo20012](https://twitter.com/duckymomo20012) - tienvinh.duong4@gmail.com

Project Link: [https://github.com/DuckyMomo20012/image-n-crypt](https://github.com/DuckyMomo20012/image-n-crypt)

<!-- Acknowledgments -->

## :gem: Acknowledgements

Here are useful resources and libraries that we have used in our projects.

- [Flask](https://flask.palletsprojects.com/): a lightweight WSGI web
  application framework.
- [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/): a Flask
  extension that provides a consistent, simple, and powerful API framework.
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/latest/):
  adds support for using JSON Web Tokens (JWT) to Flask for protecting routes.
- [Awesome Readme Template](https://github.com/Louis3797/awesome-readme-template):
  A detailed template to bootstrap your README file quickly.
