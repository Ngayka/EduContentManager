from .base import *

ALLOWED_HOSTS=["127.0.0.1", "localhost"]
DEBUG=True

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR / "db.sqlite3"),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'