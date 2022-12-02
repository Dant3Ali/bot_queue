from aiogram import Bot, types, asyncio, Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ContentType, Message
from aiogram.utils.markdown import hlink
import logging
import config
import keyboard
import sqlite3 as sql
from states import *
import func
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
storage=MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
admin=951378262, 405405526
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
count = 0
text = ''
flag = False
predmet = ''
@dp.message_handler(commands=['start'], state = None)
async def start(message):
    text1 = f"Добро жопаловать {message.from_user.first_name}（＾・ω・＾❁）"
    text2 = f"Добро пожаловать {message.from_user.first_name}(^≗ω≗^)"
    info = func.user(message.chat.id)
    if info is None:
        con = sql.connect("users.db")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS `users` (id INT PRIMARY KEY, login TEXT, Nick TEXT, stat INT, message TEXT)")
            cur.execute(f"INSERT OR IGNORE INTO `users` VALUES (?, ?, ?, ?, ?)",(message.chat.id, message.from_user.username, message.from_user.first_name, 0, 0))
            con.commit()
            info1 = func.user(message.chat.id)
            with open("Амогус.PNG", 'rb') as photo:
                if (str(info1[0]) == str(951378262) or str(info1[0]) == str(405405526)):
                    await bot.send_photo(photo=photo, chat_id=info[0], caption=text2,reply_markup = keyboard.foradmin)
                else:
                    await bot.send_photo(photo=photo, chat_id=info[0], caption=text1,reply_markup = keyboard.sotr)

    elif (str(info[0]) == str(951378262) or str(info[0]) == str(405405526)):
        with open("Амогус.PNG", 'rb') as photo:
            await bot.send_photo(photo=photo, chat_id=info[0], caption=text2, reply_markup = keyboard.foradmin)
    else:
        with open("Амогус.PNG", 'rb') as photo:
            await bot.send_photo(photo=photo, chat_id=info[0], caption=text1, reply_markup = keyboard.sotr)

#####################################################

@dp.message_handler(content_types=['text'])
async def get_message(message, state: FSMContext):
    global count
    global text
    global flag
    global predmet
    info = func.user(message.chat.id)
    if info is not None:
        if message.text =='Создать очередь 🤰':
            if (str(info[0]) == str(951378262) or str(info[0]) == str(405405526)):
                await message.answer('Введите предмет по которой будет лаба', reply_markup = keyboard.otm, parse_mode='Markdown')
                await change.Q1.set()
                func.clean()
                count = 0
                text = ''
                flag = True
            else:
                await message.answer('Куда лезем')
        elif message.text =='👨‍❤️‍👨Запись в очередь👨‍❤️‍👨':
            if flag == True:
                idn = info[0]
                fl = func.findgandona(idn)
                if fl == True:
                    await message.answer("Ты уже записался(^._.^)")
                else:
                    if count > 0:
                        func.makequeue(message.chat.id)
                        count += 1
                        await message.answer("Запись прошла успешно, но ты не первый <b>(๑✪ᆺ✪๑)</b>")
                    else:
                        func.makequeue(message.chat.id)
                        count += 1
                        await message.answer("Отныне ты самая быстрая рука на диком западе, записал тебя первым ковбой 😎")
            else:
                await message.answer("Подожди пока один из админов не создаст очередь")
        elif message.text =='Посмотреть очередь 🧐':
            if flag == True:
                if count > 0:
                    k = 1
                    for i in range(count):
                        tmp = f' <b>{func.queue[k-1]}</b>\n'
                        tmp = tmp.replace('[', '')
                        tmp = tmp.replace(']', '')
                        tmp = tmp.replace(',', '')
                        tmp = tmp.replace('(', '')
                        tmp = tmp.replace(')', '')
                        tmp = tmp.replace("'", '')
                        text += f'{k}) <b>{tmp}</b>\n'
                        k += 1
                    await message.answer(f'Очередь~~~~~ \nПредмет: <s>{predmet}</s> \n{text}', parse_mode = 'HTML')
                    text = ''
                else:
                    await message.answer("Очередь пуста , запишись первым")
            else:
                await message.answer("Подожди пока один из админов не создаст очередь")
                await message.answer("https://t.me/sskrolkina")
        elif message.text =='🤬Помощь🤬':
            texti = "https://t.me/sterakare"
            await message.answer(texti)
        elif message.text =='Технические проблемы':
            texti = "https://t.me/sterakare"
            await message.answer(texti)
        else:
            await message.answer("aboba")

#####################################################

@dp.callback_query_handler(text_contains='otm',state='*')
async def otm(call: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'OK')

#####################################################

@dp.message_handler(state=change.Q1)
async def c(message, state: FSMContext):
    global predmet
    if 'Отменить' == message.text:
        await state.finish()
        await message.answer('Главная', reply_markup=keyboard.foradmin,  parse_mode='Markdown')
        return
    async with state.proxy() as data:
        data['Q1'] = message.text
        predmet = message.text
    async with state.proxy() as data:
        Q1 = data.get("Q1")
        func.safemessage(951378262,Q1)
        await message.answer('Изменение сохранено', reply_markup=keyboard.foradmin)
        info=func.user(message.chat.id)
        receive_users, block_users = 0, 0
        spisok = func.spisok(0)
        text = "Админ добавил новую очередь скорее записывайся , чтобы успеть первым!!!"
        for user1 in spisok:
            try:
                await bot.send_message(user1[0], text)
                receive_users += 1
            except:
                block_users += 1
            await asyncio.sleep(0.4)
        await state.finish()

#####################################################

@dp.callback_query_handler(text_contains='cancle')
async def cancle(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard.sotr, parse_mode='Markdown')

###############################################################################
async def on_startup(_):
    print('Бот начал работу')

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    except Exception as e:
        print('Ошибка 18', e)
