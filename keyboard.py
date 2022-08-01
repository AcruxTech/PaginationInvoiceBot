from aiogram import types

buttons = [
  types.InlineKeyboardButton(text='<-', callback_data='-'),
  types.InlineKeyboardButton(text='Купить', callback_data='buy'),
  types.InlineKeyboardButton(text='->', callback_data='+')
]
keyboard = types.InlineKeyboardMarkup()
keyboard.add(*buttons)