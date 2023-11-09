from aiogram import types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import F
from telegram_bot.routers.hello_router import hello_router as router
from telegram_bot.states.user_states import UserState
from ml_block.start_ml import generate_text
from telegram_bot.keyboards.quarry import quarry_kb
from visualization.smiles_visulization import visualise
import telegram_bot.callbacks.start_callback
from aiogram.types import FSInputFile

@router.message(Command("start"))
async def handle_start_command(msg: Message, state: FSMContext):
  await msg.answer(text="Привет 🤗. Я могу сгенерировать молекулу по твоему описанию.. 👉🏻👈🏻. Просто начни работу", reply_markup=quarry_kb)
  
  
  
  
@router.message(UserState.main_state)
async def handle_quarry(msg: Message):
  
  gen_msg = await msg.answer("Подождите немного, я генерирую ответ... 🕐")
  
  smiles = generate_text(msg.text)
  path_to_formula = visualise(smiles) 
  
        
  await gen_msg.edit_text("Твоя формула: ")
  
  await msg.answer(smiles)
  
  await msg.answer_photo(FSInputFile(path_to_formula))
  
  