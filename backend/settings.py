import os
from pathlib import Path
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT= os.path.join(BASE_DIR,'build')
MEDIA_URL='/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'
STATICFILES_DIRS=[
  os.path.join(BASE_DIR,'build/static'),
]





# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e%tpa@js(0uidjyxn5j2q7g^nf&co6yet)w0xsvvp^l40qp1#6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'course',
    'rest_framework',
    # 'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'djoser',
    'corsheaders',
    'jazzmin',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'course.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]
CORS_ORIGIN_ALLOW_ALL = True
 
ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'build')],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_final_6',
        'USER': 'postgres',
        'PASSWORD':'admin',
        'HOST':'localhost',
        'PORT':'5432'
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST='smtp.gmail.com'
# EMAIL_PORT=587
# EMAIL_HOST_USER='jinanalkordi9@gmail.com'
# EMAIL_HOST_PASSWORD='jinanjinanjinan123123'
# EMAIL_USE_TLS=True



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


SMEDIA_ROOT= os.path.join(BASE_DIR,'media')
#MEDIA_URL='/media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
 "http://localhost:3000",
"http://127.0.0.1:3000",
]

# CORS_ALLOWED_WHITELIST = [
# "http://localhost:3000",
# "http://127.0.0.1:3000",
# ]

# CORS_ALLOW_METHODS = [
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT',
# ]
CORS_ALLOW_METHODS=[
    '*',
]

CORS_ALOW_HEADERS=[
    '*',
]

AUTH_USER_MODEL='course.UserAccount'

CORS_ALLOW_CREDENTIALS=True

CSRF_TRUSTED_ORIGINS = ['http://localhost:3000','http://localhost:8000',]

CSRF_COOKIE_DOMAIN = ['http://localhost:3000',]




REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':[
        # 'rest_framework.permissions.IsAuthenticated',
        #'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication', 
         'rest_framework_simplejwt.authentication.JWTAuthentication',
        #  'rest_framework.authentication.TokenAuthentication',
        #  'rest_framework.authentication.SessionAuthentication',
    ),
}
SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('Token',),
}
REST_USE_JWT = True
DJOSER={
    'LOGIN_FIELD':'name',
    'USER_CREATE_PASSWORD_RETYPE':True,
    # 'USERNAME_CHANGED_EMAIL_CONFIRMATION':True,
    # 'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True,
    # 'SEND_CONFIRMATION_EMAIL':True,
    # 'SET_USERNAME_RETYPE':True,
    # 'SET_PASSWORD_RETYPE':True,
    # 'PASSWORD_RESET_CONFIRM_URL':'password/reset/confirm/{uid}/{token}',
    # 'USERNAME_RESET_CONFIRM_URL':'email/reset/confirm/{uid}/{token}',
    # 'ACTIVATION_URL':'activate/{uid}/{token}',
    # 'SEND_ACTIVATION_EMAIL':True,
    'SERIALIZERS':{
        'user_create':'course.serializers.UserCreateSerializer',
        'user':'course.serializers.UserCreateSerializer',
        'user_delete':'djoser.serializers.UserDeleteSerializer',

    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': 'your_secret_key',  # Replace with your secret key
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}



CSRF_TRUSTED_ORIGINS = ['http://localhost:3000', 'http://localhost:8000']


CORS_ALLOW_ALL_ORIGINS=True


# 
