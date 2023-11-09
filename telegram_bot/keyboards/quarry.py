from aiogram import types

quarry = [
  [
    types.InlineKeyboardButton(
      text="Начать работу ✅",
      callback_data="start"
    )
  ]
]

quarry_kb = types.InlineKeyboardMarkup(
  inline_keyboard=quarry
)