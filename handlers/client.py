from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

import keyBoard.keyboard
from bot_instance import dp, bot
from parser import tv_show

async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello : {message.from_user.full_name}', reply_markup=keyBoard.keyboard.keyboard_start)


#1

async def games_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующая задача",
                                         callback_data='next_task1')
    markup.add(button_call_1)
    question = 'Сколько костей в теле взрослого человека?'
    answers = ['205—208 костей', '250-252 кости', '306-310 костей', 'у человека нет костей']
    photo = open('media/skeleton.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)
    await bot.send_poll(
        message.chat.id,
                        question=question,
                        options=answers,
                        correct_option_id=0,
                        is_anonymous = False,
                        type='quiz',
                        reply_markup=markup,
                        open_period=30,
                        explanation='Это очень легкий вопрос, если не знаешь, то загугли',
                        explanation_parse_mode = ParseMode.MARKDOWN_V2
    )

async def parser_manas_film(message: types.Message):
    data = tv_show.parser()
    for i in data:
        await bot.send_message(message.chat.id, i)

def register_handlers_client(dp:Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(games_1, commands=['games'])
    dp.register_message_handler(parser_manas_film, commands=['parser'])
