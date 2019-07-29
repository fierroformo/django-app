# Sample
API made with Django 2.2


## Prerequisites
+ [Docker 1.13 or greater](https://www.docker.com)
+ [Docker Compose 1.8.0 or greater](https://docs.docker.com/compose/)


## Install
1. Download the repository's tarball and extract it to your project's directory

    ```bash
    $ mkdir myproject
    $ cd myproject
    $ wget https://github.com/fierroformo/django-app/archive/master.tar.gz -O - | tar -xz --strip 1
    ```

2. Build docker environment

    ```bash
    $ docker-compose build
    ```

3. Init docker environment

    ```bash
    $ docker-compose up
    ```


## Environments
ENVIRONMENT | STATIC URL | SSH SERVER
------------ | ------------- | -------------
Local | [http://127.0.0.1:8000](http://127.0.0.1:8000) | docker exec -it django_app bash


## Basic commands

### Access to database

    ```bash
    $ docker exec -it django_app_db bash -c "psql -U postgres"
    ```


### Make app

    ```bash
    $ docker exec -it django_app bash -c "python manage.py startapp <app_name>"
    ```


### Make migrations

    ```bash
    $ docker exec -it django_app bash -c "python manage.py makemigrations <app_name>"
    ```


### Run migrations

    ```bash
    $ docker exec -it django_app bash -c "python manage.py migrate <app_name>"
    ```


### Load fixtures

    ```bash
    docker exec -it django_app bash -c "python manage.py loaddata <fixture>"
    ```

