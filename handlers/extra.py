from aiogram import types, Dispatcher
from bot_instance import bot


async def secret_word(message: types.Message):
    await message.reply('Привет')

async def secret_word2(message: types.Message):
    await message.reply('Кушаю')

async def secret_word3(message: types.Message):
    await message.reply('Картощечку')


async def echo_and_ban(message: types.Message):
    ban_words = ['bitch', 'slut', 'java', 'python is bad']
    for i in ban_words:
        if i in message.text.lower().replace(" ", " "):
            await message.delete()
            await bot.send_message(message.chat.id, "Вы забанены ")
            # await message.reply('This is bad word')
            # await bot.delete_message(message.chat.id, message.message_id)
        if message.text.lower() == 'dice':
            await bot.send_dice(message.chat.id, emoji='')


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(secret_word, lambda word: 'Эй, bot' in word.text)
    dp.register_message_handler(secret_word2, lambda word: 'Что делаешь?' in word.text)
    dp.register_message_handler(secret_word3, lambda word: 'Что кушаешь?' in word.text)
    dp.register_message_handler(echo_and_ban, content_types=['text'])

