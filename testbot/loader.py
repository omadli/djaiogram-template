from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from .config import API_TOKEN
from aiogram.bot.api import check_token


if not check_token(API_TOKEN):
    raise Exception("API_TOKEN not valid!")

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML, validate_token=True)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

