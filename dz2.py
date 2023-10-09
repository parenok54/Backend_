from aiogram import Bot, Dispatcher, types, executor
from config import token2
from logging import basicConfig, INFO


bot = Bot(token=token2)
dp = Dispatcher(bot)
basicConfig(level=INFO)


start_keyboards = [
    types.KeyboardButton("О нас"),
    types.KeyboardButton("ОбЪекты"),
    types.KeyboardButton("Контакты"),
]
start_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_keyboards)

@dp.message_handler(commands='start')
async def start(message:types.Message):
   await message.answer(f"Здравствуйте, {message.from_user.full_name} вас приветсвует Визион Групп", reply_markup=start_button)
   print(message)

@dp.message_handler(text="О нас")
async def about(message:types.Message):
    await message.answer("""Мы - развивающаяся компания, которая предлагает своим клиентам широкий выбор квартир в объектах расположенных во всех наиболее привлекательных районах городов Ош и Джалал-Абад. У нас максимально выгодные условия, гибкий (индивидуальный) подход при реализации жилой и коммерческой недвижимости. Мы занимаем лидирующие позиции по количеству объектов по югу Кыргызстана. Наша миссия: Мы обеспечиваем население удобным жильем для всей семьи, проявляя лояльность и индивидуальный подход и обеспечивая высокий уровень обслуживания. Мы обеспечиваем бизнес подходящим коммерческим помещением, используя современные решения и опыт профессионалов своего дела.""")


@dp.message_handler(text="Контакты")
async def contacts(message:types.Message):
    await message.answer("""г.Ош, ул.Аматова 1, Бизнес центр Томирис

contact@vg-stroy.com
+996 709 620088
+996 772 620088
+996 550 620088""")

executor.start_polling(dp)