import os
import sys
from pathlib import (
    Path,
)

FACILITY_NAME = "narayaneeyam"

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-b84o3pdb%^bt(jiwvzt$37xe%h(7xzj!bmw8p%zp8ucmpw#ur0"

DEBUG = True  # TODO

ALLOWED_HOSTS = []

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "phonenumber_field",
    "django_hashids",
    "bootstrap4",
    "rest_framework",
    "corsheaders",
]

FIRST_PARTY_APPS = [
    "ayuh_consultation",
    "ayuh_core",
    "ayuh_home",
    "ayuh_inventory",
    "ayuh_patient",
    "ayuh_staff",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + FIRST_PARTY_APPS

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


ROOT_URLCONF = "ayuh.urls"

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
            ],
            "debug": True,
        },
    },
]

WSGI_APPLICATION = "ayuh.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "narayaneeyam",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "host.docker.internal",
        "PORT": "5432",
    }
}

AUTH_USER_MODEL = "ayuh_core.AyuhUser"

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


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

DJANGO_HASHIDS_SALT = "my_salt"
DJANGO_HASHIDS_MIN_LENGTH = 5
DJANGO_HASHIDS_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"}

LOGIN_URL = f"/{FACILITY_NAME}/login/"  # IMPORTANT: start with `/`
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = f"/{FACILITY_NAME}/login/"

SPECTACULAR_SETTINGS = {
    "TITLE": f"{FACILITY_NAME.upper()} API",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "SWAGGER_UI_SETTINGS": {"displayRequestDuration": True},
}


LOGS_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} | {asctime} | {module} | {message}",
            "style": "{",
        }
    },
    "handlers": {
        "ayuh_handler": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "ayuh.log"),
            "formatter": "verbose",
        },
        "ayuh_core_handler": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "ayuh_core.log"),
            "formatter": "verbose",
        },
        "ayuh_consultation_handler": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "ayuh_consultation.log"),
            "formatter": "verbose",
        },
        "ayuh_home_handler": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "ayuh_home.log"),
            "formatter": "verbose",
        },
        "ayuh_inventory_handler": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "ayuh_inventory.log"),
            "formatter": "verbose",
        },
        "ayuh_patient_handler": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "ayuh_patient.log"),
            "formatter": "verbose",
        },
        "ayuh_staff_handler": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "ayuh_patient.log"),
            "formatter": "verbose",
        },
        "error_handler": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "error.log"),
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["error_handler"],
            "level": "ERROR",
            "propagate": True,
        },
        "ayuh": {
            "handlers": ["ayuh_handler"],
            "level": "DEBUG",
            "propagate": True,
        },
        "ayuh_core": {
            "handlers": ["ayuh_core_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
        "ayuh_consultation": {
            "handlers": ["ayuh_consultation_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
        "ayuh_home": {
            "handlers": ["ayuh_home_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
        "ayuh_inventory": {
            "handlers": ["ayuh_inventory_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
        "ayuh_patient": {
            "handlers": ["ayuh_patient_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
        "ayuh_staff": {
            "handlers": ["ayuh_staff_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}


ENABLE_DEBUG_TOOLBAR = DEBUG and "test" not in sys.argv

if ENABLE_DEBUG_TOOLBAR:
    # By default, the Django Debug Toolbar only shows on localhost or 127.0.0.1.
    # Since Docker uses a separate network, you'll need to set the INTERNAL_IPS to allow it to work within Docker.
    INTERNAL_IPS = [
        "127.0.0.1",
        "::1",
    ]

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    }

    INSTALLED_APPS += [
        "debug_toolbar",
    ]

    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]


NARAYANEEYAM_SETTINGS = {"PATIENT_CONSENT_MANDATORY": True}
