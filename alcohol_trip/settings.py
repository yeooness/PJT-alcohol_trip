"""
Django settings for alcohol_trip project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG") == "True"

ALLOWED_HOSTS = ["127.0.0.1", "localhost", ".herokuapp.com"]


# Application definition

INSTALLED_APPS = [
    'accounts',
    'bars',
    'django_bootstrap5',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'imagekit',
    'django.contrib.sites',  # 사이트 정보를 설정하기 위해 필요
    # allauth 관련 앱 목록 추가
    "allauth",
    "allauth.account",  # 가입한 계정을 관리하기 위한 것.
    "allauth.socialaccount",  # 소셜 계정을 관리하기 위한 것
    # 사용할 외부기능을 추가한다.
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.kakao',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
SOCIALACCOUNT_AUTO_SIGNUP=False
SOCIALACCOUNT_LOGIN_ON_GET=False
SOCIALACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_USERNAME_REQUIRED=True
ACCOUNT_UNIQUE_EMAIL=True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        }
    }, 

    'naver': {
        'SCOPE': [
            'profile_image',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        }
    },

    'kakao': {
        'SCOPE': [
            'profile_image',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        }
    }
}

LOGIN_REDIRECT_URL = '/bars/'

ROOT_URLCONF = "alcohol_trip.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "alcohol_trip.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 7
LOGIN_REDIRECT_URL = '/accounts'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
AUTH_USER_MODEL = "accounts.User"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_ROOT = BASE_DIR / 'images'
MEDIA_URL = '/media/'

# naver
# client key : hgD9ymV7P0RHFNuOlyZD
# Client Secret : sNpKVrNutM

# google
# client key : 409441996370-4snlkk69k42b3o12vkg8tgmsqtgun358.apps.googleusercontent.com
# Client Secret : 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

# kakao 
# rest api key : d25e65bf3dd75c3d15cb6ca941b39899

# main page : http://127.0.0.1:8000
# redirect : http://127.0.0.1:8000/accounts/login/naver/callback/

