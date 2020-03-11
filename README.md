# Project Beer404

![Icon](./icon.png)

## Table Of Contents

- [Project Beer404](#project-beer404)
  - [Table Of Contents](#table-of-contents)
  - [Description](#description)
  - [Branch System](#branch-system)
  - [Requirements](#requirements)
    - [Install command](#install-command)
  - [Access](#access)
  - [Build and Deploy](#build-and-deploy)
    - [Local Build and Deploy : Docker](#local-build-and-deploy--docker)
      - [Docker for development](#docker-for-development)
      - [Docker for production](#docker-for-production)
    - [Local Build and Deploy : Windows or Linux](#local-build-and-deploy--windows-or-linux)
    - [Production Build and Deploy : GitHub and Heroku](#production-build-and-deploy--github-and-heroku)

- [Conception](./concept/README.md)
- [Management](./manage/task.md)
- [Database](./doc/database.md)
- [Command](./doc/command.md)

## Description

The project **Beer404** is a evenemtial web application for view and manage events in the world. With this project you can without an account consult all events in the world, with an account you can create and manage your events.

## Branch System

There are a branch system for the project **Beer404** :

- Branch **master** : Development branch
- Branch **release** : Production branch for deployment
- Branch **feature_name** : Feature branch for each feature

## Requirements

Requirements List :

- Python :
  - django
  - django-extensions
  - django-debug-toolbar
- SQLite : (local database)

### Install command

    # Don't use this command, use Pipenv to setup local project !
    pip install -r ./requirements.txt

    # For SQLite linker
    sudo apt-get update && sudo apt-get install -y libsqlite3-dev

## Access

- Access in local **development** :
  - [Web Application](http://localhost:8010)
  - [Admin Panel](http://localhost:8010/admin)
  - **Admin Account** :
    - **ID** : beer
    - **Password** : 404
- Access in **production** :
  - [Web Application](http://heroku.fr)
  - [Admin Panel](http://heroku.fr/admin)

## Build and Deploy

All build and deploy command must be do in **src** folder !

### Local Build and Deploy : Docker

#### Docker for development

    # Start
    docker-compose -f ./beer404_dev.yml up -d

    # Stop
    docker-compose -f ./beer404_dev.yml down

#### Docker for production

    # Start
    docker-compose -f ./beer404_prod.yml up -d

    # Stop
    docker-compose -f ./beer404_prod.yml down

### Local Build and Deploy : Windows or Linux

    pip install --user pipenv

    pipenv install

    pipenv shell

    cd beer404

    python manage.py migrate && python manage.py runserver 0.0.0.0:8010

### Production Build and Deploy : GitHub and Heroku

- [GitHub Link](https://github.com/Fantome071/beer404)
- [Heroku Link](https://github.com/Fantome071/beer404)
