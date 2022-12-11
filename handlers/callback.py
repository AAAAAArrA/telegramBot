from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from bot_instance import  bot

async def games_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Следующая задача', callback_data='next_task2')
    markup.add(button_call_2)
    question2 = 'Какая часть мозга отвечает за сон?'
    answers = ['Лимбическая система', 'Мозжечок', 'Гипоталамус', 'Височная доля']
    photo = open('media/brain.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
                            question=question2,
                            options=answers,
                            correct_option_id=2,
                            open_period=30,
                            explanation='Ответ : 2',
                            explanation_parse_mode=ParseMode.MARKDOWN_V2,
                            is_anonymous=False,
                            type='quiz',
                            reply_markup=markup
    )
#3

async def task_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Следующая задача", callback_data='next_task3')
    markup.add(button_call_3)
    question3 = 'Какой самый крупный внутренний орган у человека?'
    answers3 = ['Мозг', 'Печень', 'Легкие', 'Мочевой пузырь']
    photo = open('media/anatomy.jpg', 'rb')
    await  bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
                            question=question3,
                            options=answers3,
                            correct_option_id=1,
                            open_period=30,
                            explanation='Что большего места в организме занимает?',
                            explanation_parse_mode=ParseMode.MARKDOWN_V2,
                            is_anonymous=False,
                            type='quiz',
                            reply_markup=markup
    )

#4

async def task_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("Следующая задача", callback_data='next_task4')
    markup.add(button_call_4)
    question4 = 'Какой самый длинный внутренний орган у человека?'
    answers4 = ['Тонкий кишечник', 'Толстый кишечник', 'Кожа']
    photo = open('media/intestine.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
                            question=question4,
                            options=answers4,
                            correct_option_id=0,
                            open_period=30,
                            explanation='Подсказака в картинке',
                            explanation_parse_mode=ParseMode.MARKDOWN_V2,
                            is_anonymous=False,
                            type='quiz',
                            reply_markup=markup
    )


async def task_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton("Следующая задача", callback_data='next_task5')
    markup.add(button_call_5)
    question5 = 'Что в человеке продолжает расти всю жизнь?'
    answers5 = ['Рост', 'зубы', 'волосы']
    photo = open('media/human.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
                            question=question5,
                            options=answers5,
                            correct_option_id=2,
                            open_period=30,
                            explanation='Это еще каждый выпадает',
                            explanation_parse_mode=ParseMode.MARKDOWN_V2,
                            is_anonymous=False,
                            type='quiz',
                            reply_markup=markup
    )

async def task_6(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton("Следующая задача", callback_data='next_task6')
    markup.add(button_call_5)
    question5 = 'Самая сильная мышца в человеческом теле?'
    answers5 = ['Прямая мышца бедра', 'Большая грудная мышца', 'Жевательная мышца']
    photo = open('media/muscle.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
                            question=question5,
                            options=answers5,
                            correct_option_id=2,
                            open_period=30,
                            explanation='Вопрос с подвохом',
                            explanation_parse_mode=ParseMode.MARKDOWN_V2,
                            is_anonymous=False,
                            type='quiz',
                            reply_markup=markup
    )

def register_handlers_callback(dp:Dispatcher):
    dp.register_callback_query_handler(games_2, lambda func: func.data == 'next_task1')
    dp.register_callback_query_handler(task_3, lambda func: func.data == 'next_task2')
    dp.register_callback_query_handler(task_4, lambda func: func.data == 'next_task3')
    dp.register_callback_query_handler(task_5, lambda func: func.data == 'next_task4')
    dp.register_callback_query_handler(task_6, lambda func: func.data == 'next_task5')
