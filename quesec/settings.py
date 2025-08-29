from pathlib import Path
import os
import environ

# ---------------------- Paths ----------------------
BASE_DIR = Path(__file__).resolve().parent.parent      # /.../src/quesec
PROJECT_DIR = BASE_DIR                                 # /.../src
REPO_DIR = PROJECT_DIR.parent                          # repo root (optional)

# ---------------------- Env ------------------------
env = environ.Env()
# Look for .env first in /src, then in repo root (works on PC & EC2)
env_file = PROJECT_DIR / ".env"
if not env_file.exists():
    alt = REPO_DIR / ".env"
    if alt.exists():
        env_file = alt
environ.Env.read_env(env_file)

# ---------------------- Core -----------------------
SECRET_KEY = env("SECRET_KEY", default="dev-change-me")
DEBUG = env.bool("DEBUG", default=True)

# Comma-separated in .env
ALLOWED_HOSTS = [h.strip() for h in env("ALLOWED_HOSTS", default="").split(",") if h.strip()]
CSRF_TRUSTED_ORIGINS = [u.strip() for u in env("CSRF_TRUSTED_ORIGINS", default="").split(",") if u.strip()]

# ---------------------- Apps/Middleware ------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "products",
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

# ---------------------- Templates ------------------
# Keep your HTML in:  /src/templates/   (home.html yahin rakho)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_DIR / "templates"],
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

# ---------------------- Database -------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME", default="quesecdata"),
        "USER": env("DB_USER", default="quesecuser"),
        "PASSWORD": env("DB_PASSWORD", default=""),
        "HOST": env("DB_HOST", default="127.0.0.1"),
        "PORT": env("DB_PORT", default="5432"),
        "CONN_MAX_AGE": 60,
    }
}

# ---------------------- i18n -----------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = env("TIME_ZONE", default="Asia/Kolkata")
USE_I18N = True
USE_TZ = True

# ---------------------- Static & Media -------------
# In prod (DEBUG=False), run: python manage.py collectstatic
STATIC_URL = "/static/"
STATIC_ROOT = PROJECT_DIR / "static"   # collectstatic target: /src/static

# Where your source assets live (Django will copy these into STATIC_ROOT)
STATICFILES_DIRS = []

from pathlib import Path
_app_static_assets = PROJECT_DIR / "quesec" / "static"/"assets"
if _app_static_assets.exists():
    # 'assets/...' URL ko 'quesec/static_assets/...' directory se map karo
    STATICFILES_DIRS.append(("assets", _app_static_assets))

# (optional) agar aapne repo-level 'assets' ya 'templates/assets' bhi rakhe hain to:
_repo_assets = PROJECT_DIR / "assets"
_templates_assets = PROJECT_DIR / "templates" / "assets"
for p in (_repo_assets, _templates_assets):
    if p.exists():
        STATICFILES_DIRS.append(p)

MEDIA_URL = "/media/"
MEDIA_ROOT = PROJECT_DIR / "media"

# ---------------------- Security (prod-friendly) ---
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE   = not DEBUG
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# ---------------------- Misc -----------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
