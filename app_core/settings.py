import os
from datetime import timedelta
from pathlib import Path
import firebase_admin
from firebase_admin import credentials

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-your-secret-key-here'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    # 🎨 Admin Paneli Tasarımı (Jazzmin)
    'jazzmin',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party Apps
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'corsheaders',
    'drf_spectacular',
    
    # Custom Apps
    'app_core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORS en üstlerde olmalı
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = 'app_core.User'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'tr-tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🔑 REST Framework Ayarları
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'app_core.authentication.FirebaseAuthentication',  # Firebase token doğrulama
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # Opsiyonel: Backend JWT
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# 🔑 Simple JWT Ayarları
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# 🌍 CORS Ayarları
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# 📖 Swagger / OpenAPI Dokümantasyon
SPECTACULAR_SETTINGS = {
    'TITLE': 'KUTEX Studios Official API',
    'DESCRIPTION': 'KUTEX Studios Mobil ve Web Uygulamaları İçin RESTful API Dokümantasyonu',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

# 🎨 Jazzmin Admin Panel Özelleştirmeleri
JAZZMIN_SETTINGS = {
    "site_title": "KUTEX Admin",
    "site_header": "KUTEX Studios",
    "site_brand": "KUTEX Studios",
    "welcome_sign": "KUTEX Studios Yönetim Paneline Hoş Geldiniz",
    "copyright": "KUTEX Studios Ltd",
    "search_model": "app_core.User",
    "topmenu_links": [
        {"name": "Ana Sayfa", "url": "admin:index", "permissions": ["auth.user"]},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "theme": "darkly",
}

# 🔥 Firebase Başlatma
if not firebase_admin._apps:
    firebase_config = {
        "type": "service_account",
        "project_id": "kutex-studios",
        "private_key_id": "6da9c7cae337fa84c6df0506d69812dd0e4a0837",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDXDwnh1BNhJ5Te\nlfOCJzrUh+POBrFZLsFP26rA4FSf0+CsflVoDLofSMrHstcDUInl9QFPMwRHAPSX\nf6lRTAsKpfiQU4YZG1JAwlO0hvjp0LzjRm2HOBlg9SME7RWcFAX/AhWBg57bFD/3\nY8htLFXtDlOxZtl44KDFq4q5ika1WKAjzqeDjhEHOIlihCRyNHns1191LBmJru4F\n3AyiWN9Ab5uYAShjyLQKG84sfxKhwJcwPuKj5+dNOkVaSOlJWQNxqZonBVXcttd4\nd0HIMDPBChsn9jzkzdtnkejib/OpnDshJW+NYt9/nYhR3jZY4pUypdbFUHldfG4K\nP0VMs8q3AgMBAAECggEAAqwrUET8RvQXrxYn9mOsajNv1AHCJHNv3Y7n/wlTyHb4\n4V4rZvfCqhNvEtNh/F2PJJLcu7te/87jqPW9mxAHkoa7fMDPQIToQcTodIgClCiz\ne6XY1lDqTGUondJXSWhBJtJDqnCCJnDR1q4yn0nXC4WLV9stxht+zR8znWrw6t1q\niKP3qpTNFpy8F6TJQtNW1ru8Dek8o0i4f3lSoVCL6z5Dk568foCKMP3mskA/PUzi\n3+hd+T47KBTAuNgK64xdWY4ypyWbm90+NAs4OFx9o1nY4vxBdJpc7Q4NIuzcv41a\na4mX5jIvgQpjby63Dk7yHqsCLtjdCLvyWRJ44Z5MmQKBgQD0vPcV+76qgfUF/aCd\nVaYyxlvYjt5Uq1Pxy2M4mCfp3bKGuxygUCickAcI+m34jKJX8L2Fb9LMrnFYiqDK\nBokgzBWcZTXGB+5ZZnkfB1hN5ezKCoyR5RvKt7zS0osKnT18biWFQcu5SciTlvCN\neYt2Wi1B2CDP9dBYsyi5nf4JmwKBgQDg9HKd4uiyGXV+seSiq5E2YNAPEkNytZqu\n7oFT0SbqlbzHZPHJj+j6ZC8AsOUH/ltlkkcpDqhax8QjIzU9szVEP8mKpgXWljum\nqdx22zQKui6HxXH4rtW7jSxdd6stFTqyBpACyhq5PvszMT/ZfxwSQlC1ZJKIndU8\nIbVXnBuTFQKBgAHJ68hmWaNnZcIQc38S5C8U0hEIIkneIrPut5/vRMNp0mc3sOLf\nExzp1JNVOT6K0Jjx8oCqK5FBaSSrhrdTSudJdpL5DmaPIkfW/uWiKRwQpSVo5FQg\np45Yv3GPBmMieROSvoV10KZfCq9BeCqgi8tmp1QG316FvmsXjCGnLPcnAoGBANth\naXnSdU5jB7PD9w4xNU+LwLxB+mce9jhNPvCn00UJPG5UYnxIjVPLag9JdEKEa0u2\nCRHgSo0lroD58A04/OSPNJSzbpQkNQ5HL0r2YV1ozsH36zsz/hqHBdItR1GTF4fQ\nYJdn1AH+iuoUyIjqrkycQat05na3PeIDmZ9UDYw1AoGAEZgmVGYuRjuHtLqbI5nY\nedvcb63o4LuLoFsEml+0shdE5ChyXToTlP3uhbGEDhvODzaGO2FA7b9RT2zOqHC/\nOL/aI5YhsLjdO+L/CzgZEbYfCKbGMBdTxZCs7wamxpHHdxt3R03p+atbFrGmUzXB\nkkexQ6d1DWD574RWnkKvfis=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-fbsvc@kutex-studios.iam.gserviceaccount.com",
        "client_id": "111143762597246242391",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40kutex-studios.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)
