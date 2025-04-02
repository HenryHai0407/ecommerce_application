# E-commerce Web Application (In Development)

## Overview

This is a simple e-commerce web application built with Django and Python, designed as a hands-on learning project. The app allows users to browse products, search for items, and view details. It’s currently in development, with two main pages implemented: a Home page and a Products page. The backend uses a MySQL database hosted on AWS RDS for persistent storage and now integrates AWS S3 for media file storage.

The goal is to eventually expand this into a fully functional e-commerce platform with features like a shopping cart and payment integration.

## Features

- **Home Page**: A welcoming landing page with a link to the Products page.
- **Products Page**: Displays a list of all products with a search bar to filter by name or description.
- **Database**: Stores product data (name, description, price, image) in a MySQL database on AWS RDS.
- **Media Support**: Product images are now stored and served from AWS S3, replacing local storage.

## Tech Stack

- **Backend**: Django (Python web framework)
- **Database**: MySQL (hosted on AWS RDS)
- **Storage**: AWS S3 (for media files)
- **Frontend**: Basic HTML templates (to be enhanced with CSS/JavaScript later)
- **Environment**: Python 3.10, virtualenv

## Project Structure
ecommerce/
├── ecommerce/          # Project settings and configuration
│   ├── init.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/          # App for product-related functionality
│   ├── migrations/    # Database migrations
│   ├── templates/     # HTML templates
│   │   └── products/
│   │       ├── home.html
│   │       └── products.html
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py      # Product model
│   ├── tests.py
│   └── views.py       # Home and Products views
├── media/             # Previously used for local images (now on S3)
├── manage.py          # Django management script
└── README.md          # This file

## Setup Instructions

### Prerequisites
- Python 3.10+
- Git
- MySQL client (e.g., `mysql` command-line tool or MySQL Workbench)
- AWS account with an RDS MySQL instance and an S3 bucket

### Steps

1. **Set Up a Virtual Environment**:
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate

2. **Install Dependencies**:
    pip install django mysqlclient boto3 django-storages

3. **Configure the Database**:
    Open inbound rules for MySQL (port 3306) in your RDS security group.
    Enable public access for the RDS instance.
    Database in settings.py:
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

4. **Configure S3 Storage**:
    Create an S3 bucket (e.g., haidebucket)
    Update settings.py with S3 settings:
        DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
        AWS_STORAGE_BUCKET_NAME = 'haidebucket'
        AWS_ACCESS_KEY_ID = 'your-access-key-id'
        AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
        AWS_S3_REGION_NAME = 'us-east-1'  # Adjust to your region
        AWS_DEFAULT_ACL = 'public-read'
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'

5. **Apply Migrations**:
    python manage.py makemigrations
    python manage.py migrate

6. **Create Superuser (for admin access)**:
    python manage.py createsuperuser

7. **Run the Development Server**:
    python manage.py runserver

8. **Access the webapp**:
    Home page: http://127.0.0.1:8000/
    Products page: http://127.0.0.1:8000/products/
------------------------------------
## Progress So Far
Set up a Django project with a products app.
Configured MySQL on AWS RDS with public access and security group rules.
Created a Product model with fields: name, description, price, and image.
Implemented basic views and templates for Home and Products pages.
Migrated media storage from local filesystem to AWS S3, including:
Synced local images to S3 using aws s3 sync.
Updated Django settings to use S3Boto3Storage for media files.
Ensured existing product image paths work with S3 URLs.
Resolved database connection issues (e.g., endpoint typos, security groups, unknown database errors).
Verified S3 integration with the UI, displaying product images from S3.

## Next Steps
Add a shopping cart feature.
Integrate a payment gateway (e.g., Stripe).
Enhance the frontend with CSS and JavaScript.
Deploy the app to a production server (e.g., AWS Elastic Beanstalk or EC2).
