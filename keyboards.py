from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_buttons = [
    [KeyboardButton(text="+"),
    KeyboardButton(text="-")],
    [KeyboardButton(text="*"),
    KeyboardButton(text="/")]
]
main_keyboard = ReplyKeyboardMarkup(keyboard=main_buttons, resize_keyboard=True, one_time_keyboard=True)

menu_buttons = [
    [KeyboardButton(text="Перейти к калькулятору")],
    [KeyboardButton(text="Мой профиль")]
]
menu_keyboard = ReplyKeyboardMarkup(keyboard=menu_buttons, resize_keyboard=True)