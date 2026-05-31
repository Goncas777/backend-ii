from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "test-secret-key"
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "blog",
]

MIDDLEWARE = []

ROOT_URLCONF = "config.urls"

TEMPLATES = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

USE_TZ = True
TIME_ZONE = "UTC"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
