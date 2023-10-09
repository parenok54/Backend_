from aiogram import Bot, Dispatcher, types, executor
from config import token
from logging import basicConfig, INFO

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

start_keyboards = [
    types.KeyboardButton("О нас"),
    types.KeyboardButton("Курсы"),
    types.KeyboardButton("График работы"),
    types.KeyboardButton("Адрес")
]
start_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_keyboards)


@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}", reply_markup=start_button)
    print(message)



@dp.message_handler(text ="О нас")
async def about(message:types.Message):
    await message.answer("""Образовательный центр Geeks (Гикс) был основан Fullstack-разработчиком Айдаром Бакировым и Android-разработчиком Нургазы Сулаймановым в 2018-ом году в Бишкеке с целью дать возможность каждому человеку, даже без опыта в технологиях, гарантированно освоить IT-профессию.

На сегодняшний день более 1200 студентов в возрасте от 12 до 45 лет изучают здесь самые популярные и востребованные IT-профессии. Филиальная сеть образовательного центра представлена в таких городах, как Бишкек, Ош и Кара-Балта.""")



@dp.message_handler(text ="График работы")
async def scheuler_time(message:types.Message):
    await message.answer(f"{message.from_user.username} наш график работы\nПН-СБ 10-00-22-00")



@dp.message_handler(text ="Адрес")
async def addres(message:types.Message):
    await message.answer("Мы находимся по адресу:\nМырзалы Аматова 1Б (Б Томирис)")
    await message.answer_location(40.51922434708214, 72.80301367977106)

courses_keyboards = [
    types.KeyboardButton("Backend"),
    types.KeyboardButton("Frontend"),
    types.KeyboardButton("Android"),
    types.KeyboardButton("IOS"),
    types.KeyboardButton("UX/UI"),
    types.KeyboardButton("Главная")

    
]
courses_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses_keyboards)

@dp.message_handler(text ="Курсы")
async def get_courses(message:types.Message):
    await message.answer("Выберите курсы:", reply_markup = courses_button)

@dp.message_handler(text ="Главная")
async def home(message:types.Message):
    await start(message)


@dp.message_handler(text ='Backend')
async def backend(message:types.Message):
    await message.answer("""Backend — это внутренняя часть сайта и сервера и т.д
Стоимость 10000 сом в месяц
Обучение: 5 месяц
""")


@dp.message_handler(text ='Frontend')
async def frontend(message:types.Message):
    await message.answer("""FrontEnd разработчик создает видимую для пользователя часть веб-страницы и его главная задача – точно передать в верстке то, что создал дизайнер, а также реализовать пользовательскую логику.
Обучение: 5 месяц
Стоимость 10000 сом в месяц
                         """)

@dp.message_handler(text ='Android')
async def android(message:types.Message):
    await message.answer("""Android-разработчик создает приложения для устройств на операционной системе Android.
Длительность: 7 месяцев
Стоимость 10000 сом в месяц""")

@dp.message_handler(text ='IOS')
async def ios(message:types.Message):
    await message.answer("""iOS-разработчик создает приложения для устройств Apple.
Длительность: 7 месяцев
Стоимость 10000 сом в месяц""")

@dp.message_handler(text ='UX/UI')
async def uxui(message:types.Message):
    await message.answer("""UX/UI дизайнер — специалист, который проектирует и рисует интерфейсы цифровых продуктов: мобильных и веб-приложений, сайтов.
Длительность: 3 месяца
Стоимость 10000 сом в месяц""")
executor.start_polling(dp)