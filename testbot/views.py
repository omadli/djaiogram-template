import logging
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from {{ app_name }}.config import SECRET_TOKEN, DEBUG
from {{ app_name }}.app import proceed_update
from asgiref.sync import async_to_sync


@csrf_exempt
@async_to_sync
async def telegram(request: HttpRequest):
    if not DEBUG:
        secret_token = request.headers.get('X-Telegram-Bot-Api-Secret-Token', None)
        if secret_token != SECRET_TOKEN:
            return HttpResponse(status=404)
    try:
        await proceed_update(request)
        return JsonResponse(data={'ok': True})
    except Exception as e:
        logging.error(e)
    return HttpResponse(status=404)
