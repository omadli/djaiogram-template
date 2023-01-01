import hashlib
from django.conf import settings
from typing import Dict

WEB_DOMAIN = settings.WEB_DOMAIN

conf: Dict = settings.DJAIOGRAM_SETTINGS.get('{{ app_name }}')
API_TOKEN: str = conf.get('API_TOKEN', None)

if API_TOKEN is None or not API_TOKEN:
    raise Exception("API_TOKEN not found!")

ADMINS = conf.get('ADMINS', [])

WEBHOOK_PATH: str = conf.get('WEBHOOK_PATH', '{{ app_name }}/')

WEBHOOK_URL = f"{WEB_DOMAIN}/{WEBHOOK_PATH}"

DEBUG = settings.DEBUG

SECRET_TOKEN = conf.get('SECRET_TOKEN', 'secret!!!')

if not DEBUG:
    if SECRET_TOKEN is None:
        SECRET_TOKEN = hashlib.pbkdf2_hmac('sha256', API_TOKEN.encode(), settings.SECRET_KEY.encode()).decode("utf-8")

