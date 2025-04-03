"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)e*4-492!e*x%96%a(d($ta4+8wdou&sg!d(sdvmjht4v*p3kk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"products/templates/products"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce_db',       # e.g., 'ecommerce_db'
        'USER': 'admin',       # e.g., 'admin'
        'PASSWORD': 'admin123+',
        'HOST': '127.0.0.1',        # e.g., 'your-db-instance.abcdef123456.us-east-1.rds.amazonaws.com'
        'PORT': '3307',
    }
}

# Credential settings: admin / Haiadmin123+

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR/ "products/static"]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Set up Media Files
import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# Ensure the media folder exists
if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)

#------- Change from LOCAL STORAGE to AWS S3
# AWS S3 Settings
# from decouple import config
# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')  # From IAM user
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')  # From IAM user
# AWS_STORAGE_BUCKET_NAME = 'haidebucket'  # Your bucket name
# AWS_S3_REGION_NAME = 'eu-north-1'  # Match your bucket’s region
# AWS_S3_FILE_OVERWRITE = False  # Prevents overwriting files with the same name
# AWS_DEFAULT_ACL = 'public-read'  # Makes uploaded files publicly readable
# AWS_S3_SIGNATURE_VERSION = 's3v4'  # Required for some regions
# AWS_STORAGE_BUCKET_NAME = 'haidebucket'
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'  # For generating URLs

# # Tell Django to use S3 for media files
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# # Media settings (for clarity)
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'  # Base URL for media files
# MEDIA_ROOT = ''  # Leave empty when using S3
