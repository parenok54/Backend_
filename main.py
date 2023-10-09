from aiogram import Bot, Dispatcher, types, executor
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет,как дела")




@dp.message_handler(commands='help')
async def get_help(message:types.Message):
    await message.answer("Вам нужна помощь?")



@dp.message_handler(text='Привет')
async def hello(message:types.Message):
    await message.answer("Привет!")


@dp.message_handler(commands='test')
async def test_bot(message:types.Message):
    await message.answer("Тест ботика")
    await message.reply("Ответ на сообщение")
    await message.answer_photo("https://static.tildacdn.com/tild3863-3635-4138-b133-613431396662/230124-237_2.jpg")
    with open ('piton.jpg', 'rb') as photo:
        await message.answer_photo(photo)
    await message.answer_location(40.51931772662277, 72.80301182274856)





@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply("Я вас не понимаю, введите /help")


executor.start_polling(dp)