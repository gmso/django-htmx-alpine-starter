# 〽️ Django + HTMX + Alpine.js starter project 〽️

> A dockerized full stack starter project using Django, plus htmx and alpine.js to give a modern SPA feel to our multi-page server-side-rendered app

Tests and CI | Code coverage | Style
:----: | :----: | :----: | 
[![Docker CI](https://github.com/gmso/django-htmx-alpine-starter/actions/workflows/docker-ci.yml/badge.svg)](https://github.com/gmso/django-htmx-alpine-starter/actions/workflows/docker-ci.yml) | [![codecov](https://codecov.io/gh/gmso/django-htmx-alpine-starter/branch/main/graph/badge.svg?token=YARRHZ5HZM)](https://codecov.io/gh/gmso/django-htmx-alpine-starter) | [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) |

## ➡️ Description

Starter project with:
- [Django 3.2](https://www.djangoproject.com/)
   - Allauth with pages (login, signup, etc.)
   - Tests for existing views, models and logic (using pytest)
   - Abstract TimeStamped base model for other models
   - Other useful packages (django-extensions, zen-queries, django-compressor, etc.)
- [HTMX 1.6.1](https://htmx.org/)
   - Used to achieve a more SPA feeling, making for a better UX
   - Starting project uses `hx-boost` to boost `<a>` and `<form>` tags, which are submitted with AJAX instead of document reloads -> Much more fluid UX
   - Beware that above point may cause old path to stick around after submitting a form. I've solved this using the `hx-push-url` attribute on each form.
- [Alpine.js 3.7.1](https://alpinejs.dev/)
   - Used mainly for only client-side interactions, adding dynamic elements, like dropdown menus.

All configured with Docker.

The docker container also configures a Postgres database for simulation a production environment.

## ➡️ Usage
Clone the repository
```
mkdir fullstack_app
cd fullstack_app
git clone https://github.com/gmso/django-htmx-alpine-starter.git
```

Then simply start the docker container to start working:
```
docker-compose up -d
```

You can then work as usual on your Django project (`localhost:8000` or `127.0.0.1:8000`).

Feel free to change existing email addresses and other configuration for your project.

## ➡️ Debugging with Docker and VSCode

Support for debugging remotely with VSCode is supported out-of-the-box.

To debug with Docker:

1. Run your Docker containers as usual: `docker-compose up -d --build`

3. Start the debug session from VS Code for the `[django:docker] runserver` configuration (either from the Debugger menu or with `F5`)

   - Logs will redirect to your integrated terminal as well.

4. Set some breakpoints in functions or methods executed when needed. Usually it's Model methods or View functions

## ➡️ Adding external libraries

It's better to install external libraries from from Docker directly
   - Production libraries
   ```
   docker-compose exec web poetry add [pip_package]
   ```
   - Development libraries
   ```
   docker-compose exec web poetry add [pip_package] --dev
   ```

## ➡️ Deploy to Heroku
### First setup
1. [Create an account](https://www.heroku.com) and [install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)  
2. Create a new app on Heroku
   ```
   heroku create
   ```
   Your app will get a randomly generated name, like _lazy-beyond-52146_. Let's call this name _[APP_NAME]_
3. Add environment variables that Django needs to read:
   1. DJANGO_ENVIRONMENT:
      ```
      heroku config:set DJANGO_ENVIRONMENT=production
      ```
   2. DJANGO_SECRET_KEY:
      You can create a safe secret key [using this site](https://djecrety.ir/)
      ```
      heroku config:set DJANGO_SECRET_KEY=[secret_key]
      ```
   3. DJANGO_DEBUG:
      ```
      heroku config:set DJANGO_DEBUG=False
      ```
   4. DJANGO_EMAIL_HOST:
      ```
      heroku config:set DJANGO_EMAIL_HOST=[your_email_host]
      ```
   5. DJANGO_EMAIL_PORT:
      ```
      heroku config:set DJANGO_EMAIL_PORT=[your_email_port]
      ```
   6. DJANGO_EMAIL_HOST_USER:
      ```
      heroku config:set DJANGO_EMAIL_HOST_USER=[your_email_host_user]
      ```
   7. DJANGO_EMAIL_HOST_PASSWORD:
      ```
      heroku config:set DJANGO_EMAIL_HOST_PASSWORD=[your_email_host_password]
      ```
4. Set the stack to Docker containers using the app's name
   ```
   heroku stack:setcontainer -a [APP_NAME]
   ```
5. Create a managed postgresql database on Heroku
   ```
   heroku addons:create heroku-postgresql:hobby-dev -a [APP_NAME]
   ```
6. Create a heroku remote repository and push changes to it
   ```
   heroku git:remote -a [APP_NAME]
   git push heroku main
   ```
7. Migrate Database and create superuser
   ```
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```
8. After deployment, check that the site's [security audit shows no warnings](https://djcheckup.com/)

### Consecutive deployments to production
Deploy by pushing to Heroku git repository:
```
git push heroku main
```
