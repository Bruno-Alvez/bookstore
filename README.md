Bookstore API

A RESTful API for managing orders and products in a bookstore application. This project was developed as part of the Backend Python course from EBAC, with a focus on clean code, scalability, and modern development practices.
Features

    🔐 Token-based authentication with Django REST Framework

    📦 Order and product management

    ✅ Automated testing with pytest

    🐳 Dockerized environment

    🚀 Continuous Integration (CI) using GitHub Actions

    ☁️ Production-ready deployment on PythonAnywhere

    🧪 Test coverage with pytest and Django's test client

    🧰 Follows best practices in software development and DevOps

Technologies

    Python 3.12

    Django 5.2

    Django REST Framework

    PostgreSQL

    Docker & Docker Compose

    Poetry

    GitHub Actions (CI/CD)

    PythonAnywhere (Deployment)

Setup and Usage
1. Clone the repository

git clone https://github.com/Bruno-Alvez/bookstore.git
cd bookstore

2. Install dependencies (using Poetry)

poetry install

3. Run local development server

poetry run python manage.py migrate
poetry run python manage.py runserver

4. Run with Docker

docker compose up -d --build
docker compose exec web python manage.py migrate

5. Run tests inside Docker

docker compose exec web python manage.py test

CI/CD

GitHub Actions is used for Continuous Integration. Every push runs the test suite automatically.
Deployment

The app is deployed on PythonAnywhere, with environment variables and a PostgreSQL database configured for production.