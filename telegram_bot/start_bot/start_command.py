from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


# Set user start bot commands

async def set_start_commands(bot: Bot):
  commands = [
    BotCommand(
      command='start',
      description='Начало работы 🐸'
    )
  ]
  
  await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())