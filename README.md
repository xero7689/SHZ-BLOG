# SHZ BLOG

This is a simple Django blog application where users can create and publish posts about various topics, and other users can view and comment on these posts. The post editor support Markdown syntax by using [Martor](https://github.com/agusmakmun/django-markdown-editor) which provides a WYSIWYG interface for writing and editing Markdown

## Table of contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- CRUD functionality for blog posts
- User profiles
- Search functionality to search through posts by different keywords
- Category and Tags functionality to classify the articles
- Support for writing posts in Markdown
- Responsive design for desktop and mobile devices

## Installtion
Clone the repository
```
git clone https://github.com/xero7689/SHZ-BLOG.git
```

## Configuration

Before running the server, you will need to create a .env file in the root directory of this project. This file will contain configuration settings for the application.

You can adjust the values to fit your own specific configuration needs.
- `APP_NAME`: The name of your Django application.
- `DEPLOY_STAGE`: Whether this is for development, testing, staging, or production.
- `IS_DEBUG`: Set to `True` during development, otherwise set to `False`.
- `DJANGO_SECRET_KEY`: Your Django secret key. This should be a long, random string that you keep private.
- `IN_CONTAINER`: Set to `True` if running the application inside a container, otherwise set to `False`.
- `CONTAINER_STORAGE_PATH`: The path where container volumes are mounted.
- `LOGGING_FILE_NAME`: The name of the log file.

- `DATABASE_URI`: The URI used to connect to the database.
- `DATABASE_DB_NAME`: The name of the database.
- `DATABASE_USER`: The username used to connect to the database.
- `DATABASE_PASSWD`: The password used to connect to the database.

- `DJANGO_SUPERUSER_USERNAME`: The username for the Django superuser account.
- `DJANGO_SUPERUSER_PASSWORD`: The password for the Django superuser account.
- `DJANGO_SUPERUSER_EMAIL`: The email address for the Django superuser account.
- `DJANGO_ADMIN_URL_PATH`: The URL path where the Django admin site will be located.

## Run the Server:
Once you have created your `.env` file, you can build the server image by running:
```
docker compose build
```
and start related services by using:
```
docker compose up
```

## Admin Super User
The default admin account for the superuser will be generated when the service is started via Docker Compose, and the values for this account will be based on the `DJANGO_SUPERUSER_XXX` attribute which is specified in the `.env` configuration file.

## DJANGO SECRET KEY
You should generate your own secret key instead of using the default one before running the server in a public environment.

You can generate a new key using the following command:
```
python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
```
