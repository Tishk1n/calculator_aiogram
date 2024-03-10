from config import TOKEN
from aiogram import Bot, Dispatcher, types
import logging
import asyncio
from aiogram import F
from keyboards import main_keyboard, menu_keyboard
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

class Calculator(StatesGroup):
    operator = State()
    sum1 = State()
    sum2 = State()
    clear = State()

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode = ParseMode.HTML)

########### Calculation Functions ################
def sum(a, b):
    i = a + b
    return str(i)

def min(a, b):
    i = a-b
    return str(i)

def multipl(a, b):
    i = a*b
    return str(i)

def division(a, b):
    i = a/b
    return str(i)

def remove_specific_characters(input_string):
    special_characters = ['{', '}', "'"]
    for char in special_characters:
        input_string = input_string.replace(char, '')
    return input_string
########################################################

@dp.message(F.text == "/start")
async def start_user(message: types.Message):
    await message.answer("Приветствую в боте!", reply_markup=menu_keyboard)

@dp.message(F.text == "Перейти к калькулятору")
async def start_calc(message: types.Message, state: FSMContext):
    await state.set_state(Calculator.operator)
    await message.answer("Выберите действие.", reply_markup=main_keyboard)

@dp.message(Calculator.operator)
async def choice_sum1(message: types.Message, state: FSMContext):
    if message.text == "Мой профиль":
        pass
    else:
        await state.update_data(operator = message.text)
    await message.answer("Введите первое число")
    await state.set_state(Calculator.sum1)

@dp.message(Calculator.sum1)
async def choice_sum2(message: types.Message, state: FSMContext):
    if message.text == "Мой профиль":
        pass
    else:
        await state.update_data(sum1 = message.text)
    await message.answer("Введите второе число")
    await state.set_state(Calculator.sum2)

@dp.message(Calculator.sum2)
async def save_data(message: types.Message, state: FSMContext):
    if message.text == "Мой профиль":
        pass
    else:
        await state.update_data(sum2 = message.text)
    data = await state.get_data()
    sum1 = float(remove_specific_characters(f"{data['sum1']}"))
    sum2 = float(remove_specific_characters(f"{data['sum2']}"))
    if f"{data['operator']}" == "+":
        await message.answer(f"Ответ: {sum(sum1, sum2)}", reply_markup=menu_keyboard)
    elif f"{data['operator']}" == "-":
        await message.answer(f"Ответ: {min(sum1, sum2)}", reply_markup=menu_keyboard)
    elif f"{data['operator']}" == "*":
        await message.answer(f"Ответ: {multipl(sum1, sum2)}", reply_markup=menu_keyboard)
    elif f"{data['operator']}" == "/":
        await message.answer(f"Ответ: {division(sum1, sum2)}", reply_markup=menu_keyboard)
    await state.set_state(Calculator.clear)

@dp.message(F.text == "Мой профиль")
async def my_profile(message: types.Message, state: FSMContext):
    data = await state.get_data()
    try:
        sum1 = float(remove_specific_characters(f"{data['sum1']}"))
        sum2 = float(remove_specific_characters(f"{data['sum2']}"))
        if f"{data['operator']}" == "+":
            await message.answer(f"<b>Приветствую в профиле, {message.from_user.full_name}!</b>\nВаш последний пример: {data['sum1']} {data['operator']} {data['sum2']} = {sum(sum1, sum2)}", reply_markup=menu_keyboard)
        elif f"{data['operator']}" == "-":
            await message.answer(f"<b>Приветствую в профиле, {message.from_user.full_name}!</b>\nВаш последний пример: {data['sum1']} {data['operator']} {data['sum2']} = {min(sum1, sum2)}", reply_markup=menu_keyboard)
        elif f"{data['operator']}" == "*":
            await message.answer(f"<b>Приветствую в профиле, {message.from_user.full_name}!</b>\nВаш последний пример: {data['sum1']} {data['operator']} {data['sum2']} = {multipl(sum1, sum2)}", reply_markup=menu_keyboard)
        elif f"{data['operator']}" == "/":
            await message.answer(f"<b>Приветствую в профиле, {message.from_user.full_name}!</b>\nВаш последний пример: {data['sum1']} {data['operator']} {data['sum2']} = {division(sum1, sum2)}", reply_markup=menu_keyboard)
    except:
        await message.answer(f"<b>Приветствую в профиле, {message.from_user.full_name}</b>!\n<tg-spoiler>Вы не вводили пример, ебанат конченный я твою мать шатал нахуй уебище ебучее лсный пидорас!</tg-spoiler>")

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())