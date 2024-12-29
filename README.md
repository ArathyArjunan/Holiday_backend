# Django Holidays API

This project is a Django-based API that fetches public holidays for a specific country and year. The holidays data is returned in JSON format, which can be consumed by front-end applications to display relevant holiday information.

## Features

- Fetch holidays data for a specific country and year.
- Return holidays with details like name, description, date, and more.
- Support for a RESTful API endpoint to interact with the holidays data.

## Technologies Used

- **Django** - A high-level Python web framework used for building the API.
- **Django Rest Framework (DRF)** - A powerful toolkit for building Web APIs.
- **SQLite** (or any other database) - Used to store holidays data (optional depending on the API's data source).
- **Python** - Programming language used for the backend logic.

## Setup Instructions

### Prerequisites

Before setting up the project, ensure you have the following software installed on your system:

- Python (>= 3.8)
- Django (>= 4.0)
- Django REST Framework (>= 3.12)
  

### 1. Clone the repository

-Clone the project repository to your local machine.

-git clone -b master https://github.com/ArathyArjunan/Holiday_backend.git
create virtual enviornment 
-python -m venv venv
-pip install -r requirements.txt
-API Request formt:http://127.0.0.1:8000/api/holidays/fetch/?country=AF&year=2024


### start server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


