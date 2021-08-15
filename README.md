# Blog Application

-- blog application backend

## Application Hosted at AWS

IP `15.206.189.128`

## Getting on-board

### Requirements for the project

1. Python >=v3.8.5
2. postgresql

### Steps to init project

1. create and activate virtualenv `virtualenv env && source env/bin/activate`
2. run `pip3 install -r requirements.txt`
3. create .env from .env.example
4. create postgres db named todo_db
5. run `python3 manage.py makemigrations`
6. run `python3 manage.py migrate`

### How to run project on localhost

1. run `python3 manage.py runserver` to start django server
2. run `python3 manage.py makemigrations` to make migrations
3. to create super user `python3 manage.py createsuperuser`
4. run `python3 manage.py migrate` to add migrations to db

### App frontend repo

[repo link](https://github.com/thisisfaisalhere/blog-frontend)
