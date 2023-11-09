from aiogram.fsm.state import StatesGroup, State

# Класс состояний

class UserState(StatesGroup):
  start_state = State()
  main_state = State()