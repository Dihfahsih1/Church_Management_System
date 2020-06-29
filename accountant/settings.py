
import os
from django.contrib.messages import constants as messages
SECRET_KEY = 't0yt9x7-+k$ix)i3)@7e0z-88me5=4yn(5%^@-=)-vg@^&%9(c'
DEBUG = True
ALLOWED_HOSTS = []
CORS_ORIGIN_ALLOW_ALL = True
APPEND_SLASH=False
INSTALLED_APPS = [
    'dashboard',
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'users.apps.UsersConfig',
    'bootstrap_datepicker_plus',
    'bootstrap4',
    'widget_tweaks',
    'live_support',
    ]
AUTH_USER_MODEL = 'dashboard.User'
MIDDLEWARE = [   
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
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'uccbwaise',
        'HOST': 'localhost',
        'PORT': '5432',
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
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_ROOT = ''
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'uccbwaise1@gmail.com'
EMAIL_HOST_PASSWORD = 'dvvzfwgpnjyttqsj'
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
GOOGLE_RECAPTCHA_SECRET_KEY = '6Ld2KqYZAAAAAMpds7Y4Zw8K5L7JkcuiSopEEtBW'
