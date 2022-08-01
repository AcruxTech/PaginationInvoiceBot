from email.message import Message
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from keyboard import keyboard

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

available_goods = ["один", "два", "три"]
current_state = 0
new_message = Message()

@dp.message_handler(commands='start')
async def message(message: types.Message):
  await message.answer('Это тестовый бот с пагинацией товаров. Для покупки нажмите /buy')

@dp.message_handler(commands='buy')
async def message(message: types.Message):
  global new_message
  new_message = await message.answer(available_goods[current_state], reply_markup=keyboard)

@dp.callback_query_handler(text='+')
async def send_random_value(call: types.CallbackQuery):
  global current_state

  if current_state < len(available_goods) - 1:
    current_state += 1 
  else:
    current_state = 0
  await new_message.edit_text(available_goods[current_state], reply_markup=keyboard)
  await call.answer()

@dp.callback_query_handler(text='-')
async def send_random_value(call: types.CallbackQuery):
  global current_state

  if current_state == 0:
    current_state = len(available_goods) - 1
  else:
    current_state -= 1
  await new_message.edit_text(available_goods[current_state], reply_markup=keyboard)
  await call.answer()

@dp.callback_query_handler(text='buy')
async def send_random_value(call: types.CallbackQuery):
  await call.answer(text='Вы купили', show_alert=True)

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)