import os
import sys
from pathlib import (
    Path,
)
import environ

APP_NAME = "narayaneeyam"

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

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
    "ayuh_admission",
    "ayuh_consultation",
    "ayuh_core",
    "ayuh_home",
    "ayuh_inventory",
    "ayuh_patient",
    "ayuh_staff",
    "ayuh_facility",
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
                "ayuh_core.context_processors.ayuh_context_processor.ayuh_context",
            ],
            "debug": True,
        },
    },
]

WSGI_APPLICATION = "ayuh.wsgi.application"

DATABASES = {
    "default": env.db(),
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


DJANGO_HASHIDS_SALT = env("DJANGO_HASHIDS_SALT")
DJANGO_HASHIDS_MIN_LENGTH = 5
DJANGO_HASHIDS_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"}

COLOR_OCHRE = "#966d29"
COLOR_WHITE = "#ffffff"

APP_PROFILES = {
    "NARAYANEEYAM": {
        "APPLICATION_FACILITY_NAME": "NARAYANEEYAM ARYA AYURVEDAM",
        "APPLICATION_MOTTO": "त्रायस्व सर्वामयात्",
        "APPLICATION_PRIMARY_COLOR": COLOR_OCHRE,
        "APPLICATION_BUTTON_TEXT_COLOR": COLOR_WHITE,
        "INVOICE_LETTERHEAD_NAME_LINE1": "Ashtavaidyan Vayaskara Krishnan Mooss Memorial",
        "INVOICE_LETTERHEAD_NAME_LINE2": "NARAYANEEYAM ARYA AYURVEDAM",
        "INVOICE_LETTERHEAD_MOTTO": "त्रायस्व सर्वामयात्",
        "INVOICE_LETTERHEAD_ADDR_LINE1": "Vayaskarakunnu, Kottayam",
        "INVOICE_LETTERHEAD_ADDR_LINE2": "Edappally, Ernakulam",
        "INVOICE_LETTERHEAD_CONTACT_PHONE": "☎ +91 8289816629",
        "INVOICE_LETTERHEAD_CONTACT_EMAIL": "✉ gopika.nkn@gmail.com",
        "INVOICE_LETTERHEAD_LOGO_IMAGE": "narayaneeyam.png",
        "INVOICE_LETTERHEAD_WEBSITE": "https://narayaneeyam.in",
        "INVOICE_SIGN_IMAGE": "",
        "INVOICE_POLICY_LINE": "Products once sold shall not be taken back.",
        "PATIENT_CONSENT_MANDATORY": False,
        "APPLY_GST": True,
        "GST_ON_CONSULTATION": 0,
        "CONSULTATION_FEE": 250,
    },
}

ACTIVE_APP_PROFILE = env("ACTIVE_APP_PROFILE")

APP_SETTINGS = APP_PROFILES[ACTIVE_APP_PROFILE]

LOGIN_URL = f"/{APP_NAME}/login/"  # IMPORTANT: start with `/`
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = f"/{APP_NAME}/login/"

SPECTACULAR_SETTINGS = {
    "TITLE": f"SMGN API",
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
        "ayuh_admission_handler": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "ayuh_admission.log"),
            "formatter": "verbose",
        },
        "ayuh_facility_handler": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "ayuh_facility.log"),
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
        "ayuh_admission": {
            "handlers": ["ayuh_admission_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
        "ayuh_facility": {
            "handlers": ["ayuh_facility_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}


ENABLE_DEBUG_TOOLBAR = DEBUG and "test" not in sys.argv  # TODO:

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
