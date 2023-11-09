from telegram_bot.routers.hello_router import hello_router as router
from telegram_bot.states.user_states import UserState
from aiogram import types
from aiogram import F
from aiogram.fsm.context import FSMContext


@router.callback_query(F.data == "start")
async def handle_start(callback: types.CallbackQuery, state: FSMContext):
  await callback.message.answer(text="Начните вводить описание молекулы (поддерживается только английский язык)♿")
  await state.set_state(UserState.main_state)
  await callback.answer()