from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
foradmin = types.ReplyKeyboardMarkup(resize_keyboard=True)
look = types.KeyboardButton('Посмотреть очередь 🧐')
create = types.KeyboardButton('Создать очередь 🤰')
view = types.KeyboardButton('👨‍❤️‍👨Запись в очередь👨‍❤️‍👨')
help = types.KeyboardButton('Технические проблемы')
newfeat = types.KeyboardButton('Выйти из очреди')
newfeat2 = types.KeyboardButton('Предложить поменяться местами')
foradmin.add(create, view, help, look, newfeat, newfeat2)
#####################################################
sotr = types.ReplyKeyboardMarkup(resize_keyboard=True)
look = types.KeyboardButton('Посмотреть очередь 🧐')
queue = types.KeyboardButton('👨‍❤️‍👨Запись в очередь👨‍❤️‍👨')
alert = types.KeyboardButton('🤬Помощь🤬')
newfeat = types.KeyboardButton('Выйти из очреди')
newfeat2 = types.KeyboardButton('Предложить поменяться местами')
sotr.add(look,queue, alert, newfeat, newfeat2)
#####################################################
otm = InlineKeyboardMarkup()
otm.add(InlineKeyboardButton('Отмена', callback_data='otm'))
