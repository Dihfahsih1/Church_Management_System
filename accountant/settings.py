
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
ALLOWED_HOSTS = ['*']
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
    #'github_storages',
    'captcha',
    'ckeditor',
    'ckeditor_uploader',
    'django_social_share',
    'django_comments_xtd',
    'django_comments',
    'taggit',
    'rest_framework',
    
    # #Social auth
    # 'allauth', 
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.twitter',
    
    
    ]

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

# DEFAULT_FILE_STORAGE='github_storages.backend.BackendStorages'
# GITHUB_HANDLE='Pythonista1'
# ACCESS_TOKEN='f284bcf2c4651226f99da98e821abfb98a24a610'
# GITHUB_REPO_NAME='amazing'
# MEDIA_BUCKET_NAME='media'

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
USE_X_FORWARDED_HOST = True
#SESSION_EXPIRE_AT_BROWSER_CLOSE = True     # opional, as this will log you out when browser is closed
SESSION_COOKIE_AGE = 60000                # 0r 10 * 60, same thing
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
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME':env("DB_NAME"),
#         'USER': env("DB_USER"),
#         'PASSWORD':env("DB_PASSWORD"),
#         'HOST': env("DB_HOST"),
#         'PORT':env("DB_PORT"),
#     }
# }
# if os.environ.get('GITHUB_WORKFLOW'):
#     DATABASES = {
#         'default': {
#           'ENGINE': 'django.db.backends.postgresql',
#           'NAME': env("DB_GIT"),
#           'USER': env("DB_USER"),
#           'PASSWORD': env("DB_PASSWORD"),
#           'HOST': env("DB_HOST"),
#           'PORT': env("DB_PORT"),
#         }
#     }
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

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# EMAIL_BACKEND = env('EMAIL_BACKEND')
# EMAIL_HOST = env('MAIL_HOST')
# EMAIL_HOST_USER = env('MAIL_USER')
# EMAIL_HOST_PASSWORD = env('MAIL_PASSWORD')
# EMAIL_USE_SSL= True
# EMAIL_PORT = 290
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER ='dihfahsihm@gmail.com'
EMAIL_HOST_PASSWORD ='desire1996?'
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


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS =[ BASE_DIR+"/assets", ]
# STATIC_ROOT = '/home/uccbwais/public_html/static'
# MEDIA_ROOT = '/home/uccbwais/public_html/media'

#Settings for development
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')



SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

 #...
SITE_ID = 1

CACHES = {
  'default': {
    'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    'LOCATION': '127.0.0.1:11211',
   }
}

####################################
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

###################################

#TRACKING WEBSITE VISITORS
TRACK_AJAX_REQUESTS = True
TRACK_ANONYMOUS_USERS =True
TRACK_SUPERUSERS = False
TRACK_PAGEVIEWS =True
TRACK_IGNORE_STATUS_CODES = [400, 404, 403, 405, 410, 500]
TRACK_REFERER = True
TRACK_QUERY_STRING = True

COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'default': {
        'allow_flagging': False,
        'allow_feedback': False,
        'show_feedback': False,
        'who_can_post': 'all'
    }
}

COMMENTS_XTD_MAX_THREAD_LEVEL = 0
COMMENTS_XTD_MARKUP_FALLBACK_FILTER = 'markdown'
COMMENTS_XTD_CONFIRM_EMAIL = False
COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_FROM_EMAIL = "church@uccbwaise.org"
COMMENTS_XTD_CONTACT_EMAIL = "church@uccbwaise.org"

#allauth app
SOCIALACCOUNT_PROVIDERS = {
    
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v10.0',
    },
        
    'google': {
        "APP": {
            "client_id": "188820696910-s9fv09qcqlsgsqjklbjhtf74akb909dj.apps.googleusercontent.com",
            "secret": "hu0l6I1zCDipaoRj2zjVF9ON", 
        },
        'SCOPE': [
        
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
    },
    
    'twitter':{}
}
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_QUERY_EMAIL = True
#ACCOUNT_ADAPTER = "users.adapters.AccountsAdapter"
SOCIALACCOUNT_AUTO_SIGNUP =True
ACCOUNT_EMAIL_VERIFICATION = 'none'

TAGGIT_CASE_INSENSITIVE = True
LOGIN_URL = 'Login/'
#ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.MembershipAccountForm'

############# GOOGLE RECAPTCHA ###############################
# SITE KEY FOR CLIENT SIDE INTEGRATION = 6LeugsUaAAAAABMI74vlJi90v5nlLOwY56WKR9wK

# SECRET KEY FOR SERVER SIDE INTEGRATION = 6LeugsUaAAAAAD_BpNftqXyAAaKut3d7AJ2bIJTO


### fix error of not loading the jquery for auto complete by downgrading to pip install django-autocomplete-light==3.5.1