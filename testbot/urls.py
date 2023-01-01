from django.urls import path
from . import views
from {{ app_name }}.config import WEBHOOK_PATH

urlpatterns = [
    path(WEBHOOK_PATH, views.telegram, name='{{ app_name }}'),
]
