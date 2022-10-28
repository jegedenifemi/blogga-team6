"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
# from dotenv import load_dotenv
import dj_database_url
from pathlib import Path
import django_heroku
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# load_dotenv(os.path.join(BASE_DIR, '.env'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '73siuk@n$yr&)_kg-bnu_t)ed=+q)*n7iq3s-s*snqrr3h9h!&'
#  os.getenv("DJANGO_SECRET_KEY")
#  config('DJANGO_SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['web-production-c906.up.railway.app/','127.0.0.1']
CSRF_TRUSTED_ORIGINS= ['https://web-production-c906.up.railway.app/']
# CORS_ALLOWED_ORIGINS =  ['web-production-c906.up.railway.app',"http://localhost:8080",
#     "http://127.0.0.1:9000",]
# Application definition

INSTALLED_APPS = [
  
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',
    # Web applications
    'accounts',
    'post',
    # 3rd party applications
    #   "corsheaders",
    'django_extensions',
    'django_summernote',
    'taggit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #  "corsheaders.middleware.CorsMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }
# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = 'postgresql://postgres:63aXtIZo1cPMZMLpk569@containers-us-west-96.railway.app:6686/railway'
DATABASES ={
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}



#DATABASES ={
#    'default': dj_database_url.config()
#}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static/')]
# STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media/'

X_FRAME_OPTIONS = 'SAMEORIGIN'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_USER = 'afariogun.john2002@gmail.com'
EMAIL_HOST_PASSWORD= 'civgsenofnujoyiq'
# os.getenv("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_USER")
# config("EMAIL_HOST_PASSWORD")
EMAIL_PORT = '465'

# django_heroku.settings(locals())
