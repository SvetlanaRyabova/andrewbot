from aiogram import types
from dispatcher import dp
from handlers import markup as nav
import asyncio
from contextlib import suppress

from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted,
                                      MessageToDeleteNotFound)


async def delete_message(message: types.Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.delete()
    msg = await message.answer('Меню', reply_markup=nav.mainMenu)
    asyncio.create_task(delete_message(msg, 6))


@dp.message_handler()
async def bot_message(message: types.Message):
    message.text.upper()
    if message.text == 'ДСМ':
        await message.answer(
            'https://teams.microsoft.com/l/meetup-join/19%3ameeting_MzUyYjdlYjgtZDhhZi00OWVkLWJhYmUtNTA3OGJlY2UwMWM3'
            '%40thread.v2/0?context=%7b%22Tid%22%3a%22e69d1d52-339c-44ae-a716-fee3bb00d48d%22%2c%22Oid%22%3a'
            '%2226624fe9-e271-43d5-9cd9-4d852d720456%22%7d', reply_markup=nav.mainMenuRemove)
    elif message.text == 'Ретро':
        await message.answer('https://miro.com/app/board/o9J_kpAq060=/?moveToWidget=3074457360941169165&cot=14',
                             reply_markup=nav.mainMenuRemove)
    elif message.text == 'Планирование':
        await message.answer('https://miro.com/app/board/uXjVOWld3wE=/', reply_markup=nav.mainMenuRemove)
    elif message.text == 'Метрики':
        await message.answer('https://docs.google.com/spreadsheets/d/14A2JXyM5KO11igAS-ynAbR6FOJv3ywP88P7KvR232bY/edit?usp=sharing',
                             reply_markup=nav.mainMenuRemove)
