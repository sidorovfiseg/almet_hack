import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

from telegram_bot.config.config_reader import config
from telegram_bot.start_bot.start_command import  set_start_commands
from telegram_bot.handlers.hello_handler import router
from aiogram.client.session.aiohttp import AiohttpSession


async def init_bot_commands(bot: Bot):
  await set_start_commands(bot=bot)


async def main():
  
  PROXY_URL = "http://10.1.18.2:3128"
  session = AiohttpSession(proxy=PROXY_URL)
  
  bot = Bot(token=config.bot_token.get_secret_value(),
            parse_mode=ParseMode.HTML, session=session)
  dp = Dispatcher(storage=MemoryStorage())
  dp.startup.register(init_bot_commands)
  dp.include_router(router=router)
  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
  
  
if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  asyncio.run(main())