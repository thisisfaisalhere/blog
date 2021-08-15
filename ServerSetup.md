# Server Setup

## IP Address

```
15.206.189.128
```

## Installing requirements

```
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx npm
```

## Clone the repos

```
git clone git@github.com:thisisfaisalhere/blog.git
git clone git@github.com:thisisfaisalhere/blog-frontend.git
```

## Setting up postgreSql

```
sudo -u postgres psql

CREATE DATABASE blog_db;
CREATE USER blog_db_user WITH PASSWORD 'password'; -- don't password as password

ALTER ROLE blog_db_user SET client_encoding TO 'utf8';
ALTER ROLE blog_db_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE blog_db_user SET timezone TO 'Asia/Kolkata';
GRANT ALL PRIVILEGES ON DATABASE blog_db TO blog_db_user;
```

## Environment setup from Backend and package installation

```
cd backend
sudo apt install python3-virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Environment setup from Frontend and package installation

```
cd frontend
sudo npm i -g yarn
yarn
```

## Setting up environment variables

1. copy .env.example and create .env in each folder
2. and add value to all keys

## Adding Tables to database

- run `python manage.py migrate` in backend folder after activating virtual environment

## Creating build and starting pm2

```
sudo npm i -g pm2 serve
pm2 start 'serve -s build' -n frontend
```

## Setting up gunicorn

### open gunicorn.service file

```
sudo nano /etc/systemd/system/gunicorn.service
```

### add gunicorn service setup details

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/blog
ExecStart=/home/ubuntu/blog/env/bin/gunicorn --access-logfile - --workers 10 --bind unix:/home/ubuntu/blog/core.sock core.wsgi:application

[Install]
WantedBy=multi-user.target
```

### set gunicorn to run on start up

```
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

### Misc commands for gnunicorn

- restart gunicron `sudo systemctl daemon-reload && sudo systemctl restart gunicorn`
- check status `sudo systemctl status gunicorn`

## setting up NGINX

### creating and opening a new server block in Nginx’s sites-available directory

```
sudo nano /etc/nginx/sites-available/blog
```

### NGINX setup

```
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    ssl_certificate         /etc/ssl/certs/cert.pem;
    ssl_certificate_key     /etc/ssl/private/key.pem;
    server_name IP;

    location / {
        proxy_pass http://localhost:5000;
    }
}

server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    ssl_certificate         /etc/ssl/certs/cert.pem;
    ssl_certificate_key     /etc/ssl/private/key.pem;
    server_name IP;

    location /static/ {
        root /home/ubuntu/blog;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/blog/core.sock;
    }
}

```

### Linking site-available to site-enable

```
sudo ln -s /etc/nginx/sites-available/blog /etc/nginx/sites-enabled
```

### Misc NGINX commands

- to restart nginx `sudo systemctl restart nginx`
- to check nginx syntax `sudo nginx -t`
