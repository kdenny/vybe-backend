# vybe-backend
The backend Django project powering the REST API and autocomplete services. This project is written using the Django REST framework

### Installation

- $ git clone https://github.com/kdenny/vybe-backend
- $ cd vybe-backend
- $ virtualenv vybeenv
- $ source vybeenv/bin/activate
- $ pip install -r requirements.txt

### DB migrations

- $ python manage.py makemigrations
- $ python manage.py migrate

### Creating a superuser

- $ python manage.py createsuperuser

### Running app

- $ python manage.py runserver