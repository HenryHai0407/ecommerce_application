E-commerce Web Application (Developing)
-----
Overview

This is a simple e-commerce web application built with Django and Python, designed as a hands-on learning project. The app allows users to browse products, search for items, and view details. It’s currently in development, with two main pages implemented: a Home page and a Products page. The backend uses a MySQL database hosted on AWS RDS for persistent storage.

The goal is to eventually expand this into a fully functional e-commerce platform with features like a shopping cart and payment integration.

------
Features
Home Page: A welcoming landing page with a link to the Products page.
Products Page: Displays a list of all products with a search bar to filter by name or description.
Database: Stores product data (name, description, price, image) in a MySQL database on AWS RDS.
Media Support: Handles product image uploads, served locally during development.

------
Tech Stack
Backend: Django (Python web framework)
Database: MySQL (hosted on AWS RDS)
Frontend: Basic HTML templates (to be enhanced with CSS/JavaScript later)
Environment: Python 3.10, virtualenv

-----
Project Structure

ecommerce/
├── ecommerce/          # Project settings and configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/          # App for product-related functionality
│   ├── migrations/    # Database migrations
│   ├── templates/     # HTML templates
│   │   └── products/
│   │       ├── home.html
│   │       └── products.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py      # Product model
│   ├── tests.py
│   └── views.py       # Home and Products views
├── media/             # Uploaded product images
├── manage.py          # Django management script
└── README.md          # This file

------
Setup Instructions

Prerequisites
    Python 3.10+
    Git
    MySQL client (e.g., mysql command-line tool or MySQL Workbench)
    AWS account with an RDS MySQL instance

1/ Setup a VENV:
2/ Install Dependencies: django, mysqlclient
3/ Configure the Database: (Open Inbound rules for MySQL, Publicly access for cloud RDS)
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'ecommerce_db',  # Your database name
            'USER': 'your_master_username',
            'PASSWORD': 'your_master_password',
            'HOST': 'your-rds-endpoint.amazonaws.com',
            'PORT': '3306',
        }
    }
4/ Apply Migrations:
python manage.py makemigrations
python manage.py migrate

5/ Create Superuser (for admin access):
python manage.py createsuperuser

6/ Run the development server:
python manager.py runserver

7/ Visit http://127.0.0.1:8000/ for homepage, http://127.0.0.1:8000/products/ for products page

------
Progress So Far
Set up a Django project with a products app.
Configured MySQL on AWS RDS with public access and security group rules.
Created a Product model with fields: name, description, price, and image.
Implemented basic views and templates for Home and Products pages.
Added media file support for product images.
Resolved database connection issues (e.g., endpoint typos, security groups, unknown database errors).

------
Next Steps
Add a shopping cart feature.
Integrate a payment gateway (e.g., Stripe).
Enhance the frontend with CSS and JavaScript.
Move media storage to AWS S3.
Deploy the app to a production server.