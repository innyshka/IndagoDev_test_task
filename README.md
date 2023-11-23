# NOTE API✈️
#### Django REST framework

## ⚙️ Installation

Python3 must be already installed.
Also install PostgreSQL and create db.

```shell
git clone https://github.com/innyshka/IndagoDev_test_task.git
cd indago_dev
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
#create .env file based on env.sample
python manage.py migrate
python manage.py runserver #starts Django server
```

## 🐳 Run with Docker

[Docker](https://www.docker.com/products/docker-desktop) should be installed.
```shell
docker-compose up --build
```

## ✅ Accessing the Application

You can now access the API by opening your web browser 
and navigating to http://localhost:8000.

#### 🔏 Test admin user
```shell
email: admin@admin.com
password: admin
```
#### 📍 Available urls
- create user api/user/register
- get access token api/user/login
- refresh token api/user/token/refresh
- verify token api/user/token/verify
- your profile api/user/me
- logout api/user/logout
-
- api/note/note/
- api/note/note/<id>/

#### 📃 Documentation
- api/doc/swagger/
- api/doc/redoc/
- api/schema


## ✨ Features
- JWT Authenticated
- Documentation is located in `/api/doc/swagger/`
- CRUD for Note 
- generates a new random title for articles every minute using `Celery`
