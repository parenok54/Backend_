# import requests
# from bs4 import BeautifulSoup
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
# from dotenv import load_dotenv
# import os, requests

# def get_exchange_rates():
#     url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     rates = {}

#     # Найдите элементы с курсами USD, EUR, RUB и KZT
#     usd_rate = soup.find('td', text='USD').find_next_sibling('td').text
#     eur_rate = soup.find('td', text='EUR').find_next_sibling('td').text
#     rub_rate = soup.find('td', text='RUB').find_next_sibling('td').text
#     kzt_rate = soup.find('td', text='KZT').find_next_sibling('td').text

#     rates['USD'] = usd_rate
#     rates['EUR'] = eur_rate
#     rates['RUB'] = rub_rate
#     rates['KZT'] = kzt_rate

#     return rates



# # Укажите свой токен
# bot_token = Bot(os.environ.get('token'))

# bot = Bot(token=bot_token)
# dp = Dispatcher(bot)
# dp.middleware.setup(LoggingMiddleware())

# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
#     item_usd = types.KeyboardButton('USD')
#     item_eur = types.KeyboardButton('EUR')
#     item_rub = types.KeyboardButton('RUB')
#     item_kzt = types.KeyboardButton('KZT')
#     markup.row(item_usd, item_eur)
#     markup.row(item_rub, item_kzt)
#     await message.answer("Выберите валюту для обмена:", reply_markup=markup)

# @dp.message_handler(lambda message: message.text in ['USD', 'EUR', 'RUB', 'KZT'])
# async def process_currency(message: types.Message):
#     await message.answer("Введите сумму для обмена:")
#     await State.EXCHANGE.set()

# @dp.message_handler(state=State.EXCHANGE)
# async def exchange_currency(message: types.Message, state: FSMContext):
#     amount = float(message.text)
#     rates = get_exchange_rates()
#     selected_currency = message.text

#     if selected_currency in rates:
#         exchange_rate = float(rates[selected_currency])
#         result = amount * exchange_rate
#         await message.answer(f"{amount} {selected_currency} = {result:.2f} KGS")
#     else:
#         await message.answer("Выберите валюту из предложенных опций.")

#     await state.finish()




from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from logging import basicConfig, INFO
import os, requests


load_dotenv('.env')

bot = Bot(os.environ.get('token'))
dp = Dispatcher(bot)


start_keyboards = [
    types.KeyboardButton(""),
    types.KeyboardButton(""),
    types.KeyboardButton(""),
]

start_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_keyboards)


@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здравстуйте {message.from_user.full_name}")