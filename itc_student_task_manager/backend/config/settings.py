from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY='dev-only-change-me'
DEBUG=True
ALLOWED_HOSTS=['*']
INSTALLED_APPS=['django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','corsheaders','rest_framework','rest_framework.authtoken','tasks']
MIDDLEWARE=['corsheaders.middleware.CorsMiddleware','django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware']
ROOT_URLCONF='config.urls'
TEMPLATES=[]
WSGI_APPLICATION='config.wsgi.application'
DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
AUTH_PASSWORD_VALIDATORS=[]
LANGUAGE_CODE='en-us'; TIME_ZONE='Asia/Phnom_Penh'; USE_I18N=True; USE_TZ=True
STATIC_URL='static/'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
CORS_ALLOW_ALL_ORIGINS=True
REST_FRAMEWORK={'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework.authentication.TokenAuthentication'],'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.IsAuthenticated']}
