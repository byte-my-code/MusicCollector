# Music Collector

A simple website/blog written with Wagtail CMS. This project is based on info gleamed from
the official [Wagtail Bakery Demo](https://github.com/wagtail/bakerydemo), and watching the
[Learn Wagtail](https://www.youtube.com/playlist?list=PLMQHMcNi6ocsS8Bfnuy_IDgJ4bHRRrvub) videos on Youtube.

## About the Basic Setup
I wanted to make the basic layout the same (or similar) to the Wagtail demo site. To do this I had to do the following:

- Create the Wagtail site in the root directory (`wagtail start website .`)
- Rename the `home` directory to `base`
- Move both `base` and `search` into the `website` directory
- Move the static/template files from both apps into the site template/static folders.
- Adjust the migrations in the base app, and rename any reference to the `home` app to `base` (in 0002 migration file)
- Adjust the app names in settings/base.py to `website.base` and `website.search`
- Prepend the search app in the `website/urls.py` file to `website.search`

*These must be done* before running `python manage.py migrate` or the system will bail with errors.