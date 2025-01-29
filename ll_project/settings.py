"""
Django settings for ll_project project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#Static File Paths
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "staticfiles",]
STATIC_ROOT = BASE_DIR /'static'

#Media Upload Paths
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 

#CKEditor Upload Path
CKEDITOR_UPLOAD_PATH = "uploads/" 

#CKEditor Configs
CKEDITOR_CONFIGS = {
    'default': {
        #Toolbar Settings
        'toolbar': [
            ['Font', 'FontSize', 'Format' ,'Bold', 'Italic', 'Underline', 'Strike', 'RemoveFormat'],  # Added 'RemoveFormat' here
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Image', 'Table'],
            ['Source', 'Maximize']
        ],
        #Look and Feel Settings
        'height': 300,
        'width': 'auto',

        #Font Settings
        'font_names': 'Arial;Calibri;Courier New;Georgia;Tahoma;Verdana;Comic Sans MS;  Times New Roman',
        'fontSize_sizes': '8px;10px;12px;14px;16px;18px;24px;36px;48px;72px',
        
    },
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2x=^ph!rk$4w@#cg@rte94m+2cakn74$7+@^njq=qkb#x*@47^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # My apps
    'digi_diaries',                            # The main app
    'accounts',                                 # User authentication app
    
    # Third party apps
    'django_bootstrap5',
    'ckeditor',
    'ckeditor_uploader',

    # Default Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'll_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'll_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#My settings
LOGIN_REDIRECT_URL = 'digi_diaries:index'
LOGOUT_REDIRECT_URL = 'digi_diaries:index'
LOGIN_URL = 'accounts:login'
