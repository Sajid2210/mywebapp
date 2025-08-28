from pathlib import Path
import os
import environ

# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent  # /.../src/quesec
PROJECT_ROOT = BASE_DIR.parent                     # /.../src
REPO_ROOT = PROJECT_ROOT.parent                    # /.../

# -----------------------------------------------------------------------------
# Env
# -----------------------------------------------------------------------------
env = environ.Env()
# .env file kept in /src (we symlinked it on server). Works locally too.
environ.Env.read_env(env_file=BASE_DIR / ".env")

# -----------------------------------------------------------------------------
# Core
# -----------------------------------------------------------------------------
SECRET_KEY = env("SECRET_KEY", default="dev-please-change-me")
DEBUG = env.bool("DEBUG", default=True)

# Comma-separated in .env: "localhost,127.0.0.1,15.207.20.154,15.207.20.154.nip.io"
ALLOWED_HOSTS = [h.strip() for h in env("ALLOWED_HOSTS", default="").split(",") if h.strip()]
CSRF_TRUSTED_ORIGINS = [o.strip() for o in env("CSRF_TRUSTED_ORIGINS", default="").split(",") if o.strip()]

# -----------------------------------------------------------------------------
# Installed apps / middleware
# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # your apps here, e.g. "shop", "core", etc.
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "quesec.urls"

# -----------------------------------------------------------------------------
# Templates  (your home.html lives in project templates)
# Keep your templates in: /src/templates/home.html
# -----------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],   # <-- /src/templates
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "quesec.wsgi.application"

# -----------------------------------------------------------------------------
# Database (PostgreSQL via .env for both local + server)
# -----------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME", default="quesecdata"),
        "USER": env("DB_USER", default="quesecuser"),
        "PASSWORD": env("DB_PASSWORD", default=""),
        "HOST": env("DB_HOST", default="127.0.0.1"),
        "PORT": env("DB_PORT", default="5432"),
        "CONN_MAX_AGE": 60,  # keep connections open (prod-friendly)
    }
}

# -----------------------------------------------------------------------------
# Password validation / i18n
# -----------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

# -----------------------------------------------------------------------------
# Static & Media
# In prod (DEBUG=False) Django won’t serve static; Nginx serves from STATIC_ROOT.
# -----------------------------------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"     # /src/static (collectstatic target)
# If you keep extra source assets (optional), uncomment and point correctly:
# STATICFILES_DIRS = [ PROJECT_ROOT / "assets" ]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"       # /src/media

# -----------------------------------------------------------------------------
# Security (safe defaults when DEBUG=False)
# -----------------------------------------------------------------------------
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# -----------------------------------------------------------------------------
# Default auto field
# -----------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
