
from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
from logging import basicConfig, INFO
import os, requests, asyncio , aioschedule

load_dotenv('.env')

bot = Bot(os.environ.get('token'))
dp = Dispatcher(bot)
basicConfig(level=INFO)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здравстуйте {message.from_user.full_name}")


@dp.message_handler(commands='btc')
async def send_btc_price(message:types.Message):
    url = 'https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response = requests.get(url=url).json()
    btc_price = response['price']
    await message.answer(f"Цена биткоина {btc_price}$")

async def scheduler():
    aioschedule.every(2).seconds.do(send_btc_price)
    while True:
        await aioschedule.run_pending()

async def on_startup(parametr):
    asyncio.create_task(scheduler())
    






executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

