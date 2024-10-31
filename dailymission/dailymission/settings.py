"""
Django settings for dailymission project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xn5yvci=mu8j2%hkj9f8l@t-3ei1@g%6v5h@*a1o@kiq*&dgn4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['3.38.208.220', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'time_missions',
    'rest_framework',
    'corsheaders',
    'accounts',
    'rest_framework.authtoken',  # Token 인증을 사용하는 경우 추가
    'board'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'dailymission.urls'

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

WSGI_APPLICATION = 'dailymission.wsgi.application'


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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CACHES 설정
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'C:/Users/sm020/Back-end/dailymission/my_cache',  # SQLite에 사용할 테이블 이름
        'OPTIONS': {
            'CACHE_TIMEOUT': 60 * 15,  # 캐시 유효 시간 설정 (예: 15분)
        }
    }
}



# Celery 설정
from celery.schedules import crontab

CELERY_BROKER_URL = 'sqla+sqlite:///celerydb.sqlite'     # SQLite 사용
CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'     # 작업 결과 저장
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

# 추가 설정 (옵션)
CELERY_TASK_TRACK_STARTED = True        # 작업 시작 상태 추적
CELERY_TASK_TIME_LIMIT = 30             # 작업 실행 제한 시간 (초)
CELERY_ACCEPT_CONTENT = ['json']        # 데이터 직렬화 포맷 설정
CELERY_TASK_SERIALIZER = 'json'         # 작업 직렬화 포맷
CELERY_RESULT_SERIALIZER = 'json'       # 결과 직렬화 포맷
CELERY_TIMEZONE = 'Asia/Seoul'          # 타임존 설정
CELERY_ENABLE_UTC = True                # UTC 시간 사용

# Celery Beat 설정: 주기적으로 실행할 작업
CELERY_BEAT_SCHEDULE = {
    'change-mission-every-1-minute': {
        'task': 'time_missions.tasks.change_mission',
        'schedule': crontab(minute='*/1'),   # 1분마다 실행
    },
}

# 이 설정이 있어야 LoginAPIView에서 생성된 토큰이 인증에 사용될 수 있습니다.
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
