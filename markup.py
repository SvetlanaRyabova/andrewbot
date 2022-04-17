from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# Main Menu
btnRetro = KeyboardButton('Ретро')
btnDsm = KeyboardButton('ДСМ')
btnPI = KeyboardButton('PI Plan')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRetro, btnDsm, btnPI)
mainMenuRemove = ReplyKeyboardRemove()