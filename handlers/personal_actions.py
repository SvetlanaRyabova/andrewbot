from aiogram import types
from dispatcher import dp
from handlers import markup as nav


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.answer('Привет DreamTeam', reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'ДСМ':
        await message.answer(
            'https://teams.microsoft.com/l/meetup-join/19%3ameeting_MzUyYjdlYjgtZDhhZi00OWVkLWJhYmUtNTA3OGJlY2UwMWM3'
            '%40thread.v2/0?context=%7b%22Tid%22%3a%22e69d1d52-339c-44ae-a716-fee3bb00d48d%22%2c%22Oid%22%3a'
            '%2226624fe9-e271-43d5-9cd9-4d852d720456%22%7d', reply_markup=nav.mainMenuRemove)
    elif message.text == 'Ретро':
        await message.answer('https://miro.com/app/board/o9J_kpAq060=/?moveToWidget=3074457360941169165&cot=14',
                             reply_markup=nav.mainMenuRemove)
    elif message.text == 'PI Plan':
        await message.answer('https://miro.com/app/board/uXjVOWld3wE=/', reply_markup=nav.mainMenuRemove)
