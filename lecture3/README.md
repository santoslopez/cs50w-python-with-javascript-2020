# Install DJango
pip3 install Django

## Create a new project / crea un proyecto principal
django-admin startproject PROJECT_NAME

## Create app Django / Crea una app dentro de la app principal
python manage.py startapp NAME_APP

## Configurations
File settings.py in code. I'll just add nameApp:

INSTALLED_APPS = [
    'addNameApp',
    ...

]

## Name projects file: views.py
So here is the default file, again, from views.py


# Create Environment
https://flask.palletsprojects.com/en/2.0.x/installation/

# Run
python manage.py runserver

# create session
python manage.py migrate
