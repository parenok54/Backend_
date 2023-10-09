import random
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from config import token1

API_TOKEN = token1

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

# Состояния разговора
START, PLAYING = range(2)

# Глобальная переменная для хранения загаданного числа
secret_number = 0

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.reply("Привет! Я загадал число от 1 до 3. Попробуй угадать.")
    global secret_number
    secret_number = random.randint(1, 3)
    await START.set()

# Обработка ответа пользователя
@dp.message_handler(lambda message: message.text.isdigit(), state=PLAYING)
async def play_game(message: types.Message, state: types.ChatState):
    user_guess = int(message.text)
    if user_guess == secret_number:
        await message.reply("Правильно, вы угадали!")
        await message.reply_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.reply("Сожалею, вы не угадали. Попробуйте ещё раз.")
        await message.reply_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")

    await state.finish()

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)



    # import random
# from aiogram import Bot, Dispatcher, types, executor
# from config import token1

# bot = Bot(token=token1)
# dp = Dispatcher(bot)

# secret_number = 0

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer("Привет, я загадал число от 1 до 3 угадайте")
#     global secret_number
#     secret_number = random.randint(1,3)



# @dp.message_handler(commands=secret_number)
# async def random(message:types.Message):
#     await message.answer("“Правильно вы отгадали")
    



# executor.start_polling(dp)
