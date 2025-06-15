import os
import sys
from pathlib import (
    Path,
)

APP_NAME = "dhanwanthari"

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = (
    "django-insecure-b84o3pdb%^bt(jiwvzt$37xe%h(7xzj!bmw8p%zp8ucmpw#ur0"  # TODO:
)

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

DJANGO_HASHIDS_SALT = "my_salt"  # TODO:
DJANGO_HASHIDS_MIN_LENGTH = 5
DJANGO_HASHIDS_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"}

COLOR_BLUE = "#35a2c4e3"
COLOR_GREEN = "#b6d73ff7"
COLOR_OCHRE = "#966d29"
COLOR_WHITE = "#ffffff"
COLOR_BLACK = "#000000"

NARAYANEEYAM_FACILITY_NAME = "NARAYANEEYAM ARYA AYURVEDAM"
NARAYANEEYAM_MOTTO = "त्रायस्व सर्वामयात्"
NARAYANEEYAM_PRIMARY_COLOR = COLOR_OCHRE
NARAYANEEYAM_BUTTON_TEXT_COLOR = COLOR_WHITE
NARAYANEEYAM_LETTERHEAD_NAME = "NARAYANEEYAM ARYA AYURVEDAM"
NARAYANEEYAM_LETTERHEAD_MOTTO = "त्रायस्व सर्वामयात्"
NARAYANEEYAM_LETTERHEAD_ADDR_LINE1 = "Vayaskara, Kottayam"
NARAYANEEYAM_LETTERHEAD_ADDR_LINE2 = "Edappally, Ernakulam"
NARAYANEEYAM_LETTERHEAD_CONTACT1 = "☎ +91 9495350727"
NARAYANEEYAM_LETTERHEAD_CONTACT2 = "✉ gopika.nkn@gmail.com"
NARAYANEEYAM_LETTERHEAD_LOGO_IMAGE = "narayaneeyam.png"
NARAYANEEYAM_PAYMENT_BANK = ""
NARAYANEEYAM_PAYMENT_ACCOUNT = ""
NARAYANEEYAM_SOFTWARE_NAME = "SMGN"
NARAYANEEYAM_SOFTWARE_VERSION = "v0.2"
NARAYANEEYAM_ICON = "narayaneeyam.png"
NARAYANEEYAM_ABN = ""
NARAYANEEYAM_APPLY_GST = True
NARAYANEEYAM_GST = "18"
NARAYANEEYAM_CONSULTATION_FEE = "250"

AYURAROGYA_FACILITY_NAME = "AYURAROGYA PTY LTD"
AYURAROGYA_MOTTO = "Healing Space For Better Living"
AYURAROGYA_PRIMARY_COLOR = COLOR_BLUE
AYURAROGYA_BUTTON_TEXT_COLOR = COLOR_WHITE
AYURAROGYA_LETTERHEAD_NAME = "AYURAROGYA PTY LTD"
AYURAROGYA_LETTERHEAD_MOTTO = "Healing Space For Better Living"
AYURAROGYA_LETTERHEAD_ADDR_LINE1 = "18 Kingscliff Avenue"
AYURAROGYA_LETTERHEAD_ADDR_LINE2 = "Clyde, Victoria 3978"
AYURAROGYA_LETTERHEAD_CONTACT1 = "☎ +61 470 432 355"
AYURAROGYA_LETTERHEAD_CONTACT2 = "✉ info@ayurarogya.com.au"
AYURAROGYA_LETTERHEAD_LOGO_IMAGE = "ayurarogya.png"
AYURAROGYA_PAYMENT_BANK = "083004"
AYURAROGYA_PAYMENT_ACCOUNT = "787255444"
AYURAROGYA_SOFTWARE_NAME = "SMGN"
AYURAROGYA_SOFTWARE_VERSION = "v0.2"
AYURAROGYA_ICON = "ayurarogya.png"
AYURAROGYA_ABN = "27 660 465 878"
AYURAROGYA_APPLY_GST = True
AYURAROGYA_GST = "10"
AYURAROGYA_CONSULTATION_FEE = "80"

NARAYANEEYAM_APP_SETTINGS = {
    "FACILITY_NAME": NARAYANEEYAM_FACILITY_NAME,
    "MOTTO": NARAYANEEYAM_MOTTO,
    "PATIENT_CONSENT_MANDATORY": False,
    "PRIMARY_COLOR": NARAYANEEYAM_PRIMARY_COLOR,
    "BUTTON_TEXT_COLOR": NARAYANEEYAM_BUTTON_TEXT_COLOR,
    "LETTERHEAD_NAME": NARAYANEEYAM_LETTERHEAD_NAME,
    "LETTERHEAD_MOTTO": NARAYANEEYAM_LETTERHEAD_MOTTO,
    "LETTERHEAD_ADDR_LINE1": NARAYANEEYAM_LETTERHEAD_ADDR_LINE1,
    "LETTERHEAD_ADDR_LINE2": NARAYANEEYAM_LETTERHEAD_ADDR_LINE2,
    "LETTERHEAD_CONTACT1": NARAYANEEYAM_LETTERHEAD_CONTACT1,
    "LETTERHEAD_CONTACT2": NARAYANEEYAM_LETTERHEAD_CONTACT2,
    "LETTERHEAD_LOGO_IMAGE": NARAYANEEYAM_LETTERHEAD_LOGO_IMAGE,
    "PAYMENT_BANK": NARAYANEEYAM_PAYMENT_BANK,
    "PAYMENT_ACCOUNT": NARAYANEEYAM_PAYMENT_ACCOUNT,
    "SOFTWARE_NAME": NARAYANEEYAM_SOFTWARE_NAME,
    "SOFTWARE_VERSION": NARAYANEEYAM_SOFTWARE_VERSION,
    "ICON": NARAYANEEYAM_ICON,
    "ABN": NARAYANEEYAM_ABN,
    "APPLY_GST": NARAYANEEYAM_APPLY_GST,
    "GST": NARAYANEEYAM_GST,
    "CONSULTATION_FEE": NARAYANEEYAM_CONSULTATION_FEE,
}

AYURAROGYA_APP_SETTINGS = {
    "FACILITY_NAME": AYURAROGYA_FACILITY_NAME,
    "MOTTO": AYURAROGYA_MOTTO,
    "PATIENT_CONSENT_MANDATORY": True,
    "PRIMARY_COLOR": AYURAROGYA_PRIMARY_COLOR,
    "BUTTON_TEXT_COLOR": AYURAROGYA_BUTTON_TEXT_COLOR,
    "LETTERHEAD_NAME": AYURAROGYA_LETTERHEAD_NAME,
    "LETTERHEAD_MOTTO": AYURAROGYA_LETTERHEAD_MOTTO,
    "LETTERHEAD_ADDR_LINE1": AYURAROGYA_LETTERHEAD_ADDR_LINE1,
    "LETTERHEAD_ADDR_LINE2": AYURAROGYA_LETTERHEAD_ADDR_LINE2,
    "LETTERHEAD_CONTACT1": AYURAROGYA_LETTERHEAD_CONTACT1,
    "LETTERHEAD_CONTACT2": AYURAROGYA_LETTERHEAD_CONTACT2,
    "LETTERHEAD_LOGO_IMAGE": AYURAROGYA_LETTERHEAD_LOGO_IMAGE,
    "PAYMENT_BANK": AYURAROGYA_PAYMENT_BANK,
    "PAYMENT_ACCOUNT": AYURAROGYA_PAYMENT_ACCOUNT,
    "SOFTWARE_NAME": AYURAROGYA_SOFTWARE_NAME,
    "SOFTWARE_VERSION": AYURAROGYA_SOFTWARE_VERSION,
    "ICON": AYURAROGYA_ICON,
    "ABN": AYURAROGYA_ABN,
    "APPLY_GST": AYURAROGYA_APPLY_GST,
    "GST": AYURAROGYA_GST,
    "CONSULTATION_FEE": AYURAROGYA_CONSULTATION_FEE,
}

APP_SETTINGS = NARAYANEEYAM_APP_SETTINGS

LOGIN_URL = f"/{APP_NAME}/login/"  # IMPORTANT: start with `/`
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = f"/{APP_NAME}/login/"

SPECTACULAR_SETTINGS = {
    "TITLE": f"{APP_SETTINGS['FACILITY_NAME'].upper()} API",
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
