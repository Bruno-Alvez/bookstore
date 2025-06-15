# Bookstore API

A fully-featured RESTful API for managing books, categories, products, and orders in an online bookstore, built with Django and Django REST Framework. This project was designed with clean architecture principles, test coverage, containerization, and deployment in mind.

## Features

- Token-based Authentication
- Book and Category Management (CRUD)
- Product and Order Modules
- Custom Serializers and Viewsets
- Admin Panel for full control
- Automated Testing with Pytest
- DevOps pipeline with Docker & GitHub Actions
- Deployed on PythonAnywhere

## Tech Stack

Language: Python 3.12  
Framework: Django, Django REST Framework  
Authentication: Token-based (DRF)  
Testing: Pytest  
Containerization: Docker, Docker Compose  
CI/CD: GitHub Actions  
Deployment: PythonAnywhere  
Dependency Management: Poetry

## Project Structure

bookstore-api/  
├── bookstore/             - Django project settings  
├── product/               - Product & category app  
├── order/                 - Order handling app  
├── env/                   - Environment-specific settings  
├── .github/               - GitHub Actions workflows  
├── Dockerfile             - Docker container definition  
├── docker-compose.yml     - Docker Compose setup  
├── pytest.ini             - Pytest configuration  
├── pyproject.toml         - Poetry dependencies  
└── README.md              - Project documentation

## Running Tests

To run all automated tests:

pytest


Includes test coverage for models, serializers, and views.

## Running Locally with Docker

docker-compose up --build


Then access the API via `http://localhost:8000/`

## Authentication

Token authentication is implemented using Django REST Framework.

To obtain a token:

POST /api/token/
{
"username": "your_username",
"password": "your_password"
}


Then include the token in your headers:

Authorization: Token your_token_here


## CI/CD Pipeline

This project uses GitHub Actions for continuous integration. The pipeline:

- Runs tests with Pytest
- Lints the codebase
- Validates the build for deployment

Configuration file: `.github/workflows/main.yml`

## Deployment

The project is deployed to PythonAnywhere using:

- Gunicorn as the WSGI server
- Static file management with collectstatic
- SQLite or PostgreSQL (depending on plan)

## Environment Variables

Sensitive settings are configured via environment variables. Example:

DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3


## License

This project is licensed under the MIT License.

## Author

Bruno Alves  
LinkedIn: https://www.linkedin.com/in/brunoalves-tech/  
GitHub: https://github.com/Bruno-Alvez/
