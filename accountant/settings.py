
import os
from django.contrib.messages import constants as messages
import environ
import calendar
from datetime import datetime
env = environ.Env()
# reading .env file
environ.Env.read_env()

SECRET_KEY = env("KEY")
DEBUG = True
ALLOWED_HOSTS = []
CORS_ORIGIN_ALLOW_ALL = True
APPEND_SLASH=True
SITE_ID = 1

INSTALLED_APPS = [
    'dashboard',
    'tracking',
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'crispy_forms',
    'users.apps.UsersConfig',
    'bootstrap_datepicker_plus',
    'bootstrap4',
    'widget_tweaks',
    'celery',
    'github_storages',
    'captcha',
    'ckeditor',
    'ckeditor_uploader',
    'django_social_share',
    'django_comments_xtd',
    'django_comments',
    ]

COMMENTS_XTD_CONFIRM_EMAIL = False
COMMENTS_APP = 'django_comments_xtd'
#  To help obfuscating comments before they are sent for confirmation.
COMMENTS_XTD_SALT = (b"Please confirm this comment. "
                     b"This has been commented through the website.")

# Source mail address used for notifications.
COMMENTS_XTD_FROM_EMAIL = "church@uccbwaise.org"

# Contact mail address to show in messages.
COMMENTS_XTD_CONTACT_EMAIL = "church@uccbwaise.org"


#captcha properties
X_FRAME_OPTIONS = 'SAMEORIGIN'
TEXT_ADDITIONAL_TAGS = ('iframe',)
TEXT_ADDITIONAL_ATTRIBUTES = ('scrolling', 'allowfullscreen', 'frameborder', 'src', 'height', 'width')
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
#CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.word_challenge'
CAPTCHA_BACKGROUND_COLOR ='blue'
CAPTCHA_FOREGROUND_COLOR = "white"
CAPTCHA_LETTER_ROTATION = (-38, 38)
CAPTCHA_NOISE_FUNCTIONS = None
#CAPTCHA_IMAGE_SIZE = '30'

#SESSION_EXPIRE_AT_BROWSER_CLOSE = True     # opional, as this will log you out when browser is closed
SESSION_COOKIE_AGE = 6000                   # 0r 10 * 60, same thing
#SESSION_SAVE_EVERY_REQUEST = True   

AUTH_USER_MODEL = 'dashboard.User'

MIDDLEWARE = [ 
    'tracking.middleware.VisitorTrackingMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']
ROOT_URLCONF = 'accountant.urls'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = BASE_DIR
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'postgres',
        'USER': 'postgres',
        'PASSWORD':'uccbwaise',
        'HOST': '127.0.0.1',
        'PORT':'5432',
    }
}
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Kampala'
USE_I18N = True
USE_L10N = True
USE_TZ = True
USE_TZ
LOGIN_URL = 'login'
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = env('MAIL_HOST')
EMAIL_HOST_PASSWORD = env('MAIL_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


CRISPY_TEMPLATE_PACK = 'bootstrap4'
BOOTSTRAP4 = {
    'include_jquery': True,
}
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


STATIC_ROOT = ''
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))




####################################
    ##  CKEDITOR CONFIGURATION ##
####################################



CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}


    ##  CKEDITOR CONFIGURATION ##
####################################

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'images/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}

X_FRAME_OPTIONS = 'SAMEORIGIN'
####################################TRACKING WEBSITE VISITORS

TRACK_AJAX_REQUESTS = True
TRACK_ANONYMOUS_USERS =True
TRACK_SUPERUSERS = False
TRACK_PAGEVIEWS =True
TRACK_IGNORE_STATUS_CODES = [400, 404, 403, 405, 410, 500]
TRACK_REFERER = True
TRACK_QUERY_STRING = True

CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False


SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_EMAIL_REQUIRED = True