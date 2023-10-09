
import random
from aiogram import Bot, Dispatcher, types, executor
from config import token1

bot = Bot(token=token1)
dp = Dispatcher(bot)

secret_number = 0

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Привет, я загадал число от 1 до 3. Угадайте.")
    global secret_number
    secret_number = random.randint(1, 3)

@dp.message_handler(commands='guess')
async def guess(message: types.Message):
    user_guess = message.text.split(' ')[1] if len(message.text.split(' ')) > 1 else None
    if user_guess and user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == secret_number:
            await message.answer("Правильно, вы угадали!")
        else:
            await message.answer("Сожалею, вы не угадали. Попробуйте ещё раз.")
    else:
        await message.answer("Введите число после команды /guess.")

executor.start_polling(dp)
