import json
from aiogram import types, Bot, Dispatcher, executor
from django.http import HttpRequest, HttpResponse
from {{ app_name }}.loader import dp, bot
from . import middlewares, filters, handlers
from .utils.notify_admins import on_startup_notify
from .utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher: Dispatcher):
    # Birlamchi komandalar (/start va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


def run_in_executor():
    '''Process Updates with long polling'''
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


async def proceed_update(request: HttpRequest) -> None:
    ''' Process Updates on webhook '''
    upd = types.Update(**(json.loads(request.body)))
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(upd)


if __name__ == '__main__':
    run_in_executor()
