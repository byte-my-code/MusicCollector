# Music Collector

A simple website/blog written with Wagtail CMS. This project is based on info gleamed from
the official [Wagtail Bakery Demo](https://github.com/wagtail/bakerydemo), and watching the
[Learn Wagtail](https://www.youtube.com/playlist?list=PLMQHMcNi6ocsS8Bfnuy_IDgJ4bHRRrvub) videos on Youtube.

This is my learing project, and will most probably contain bugs/errors and may not adhere to best practices! I
plan to add to it as I learn new parts of the Wagtail ecosystem, and therefore parts are likely to change over
the course of the project. Most of the focus will be on the backend code rather than the frontend style.

In also plan to have a live version once I have the basics done first.

## About the Basic Setup
I wanted to make the basic layout the same (or similar) to the Wagtail demo site. To do this I had to do the following:

- Create the Wagtail site in the root directory (`wagtail start website .`)
- Rename the `home` directory to `base`
- Move both `base` and `search` into the `website` directory
- Move the static/template files from both apps into the site template/static folders.
- Adjust the migrations in the base app, and rename any reference to the `home` app to `base` (in 0002 migration file)
- Adjust the app names in settings/base.py to `website.base` and `website.search`
- Prepend the search app in the `website/urls.py` file to `website.search`

**These must be done** before running `python manage.py migrate` or the system will bail with errors.

## Running Locally
- Clone the repo somewhere (ie `~/Sites/`)
- Change into the directory (`cd musiccollector`)
- Create a virtualenv (mkvirtualenv or pipenv)
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`
- (In another shell) `npm run-script run` (this will watch the filetree for changes)

You should be able to visit the homepage at [http://127.0.0.1:8000](http://127.0.0.1:8000)