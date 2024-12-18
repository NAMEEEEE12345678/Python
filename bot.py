import asyncio
import logging
from aiogram import Bot, Dispatcher, types,F
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ContentType
import random
import requests
import subprocess
logging.basicConfig(level=logging.INFO)
bot = Bot(token='7877130154:AAGbv3ImLx3AX8J-W8ZaLG9VkK-yPZr4G1w')
dp = Dispatcher()
# @dp.message(Command("weather"))
# async def start_command(message:types.Message):
#       await message.answer("Выберите город для погоды?" )
# @dp.message(F.text)
# async def get_weather(message:types.Message):
#     city = message.text
#     try:
#         url = f"https://api.openweathermap.org/data/2.5/weather?q=%7Bcity%7D&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347"
#         weather_data = requests.get(url).json()
        
#         temperature = weather_data["main"]["temp"]
#         temperature_feels = weather_data["main"]["feels_like"]
#         wind_speed = weather_data["wind"]['speed']
#         cloud_cover = weather_data['weather'][0]['discription']
#         humidity = weather_data['main']['humidity']

#         await message.answer(f"Температура воздуха:{temperature}\n"
#                          f"Ощущается как:{temperature_feels}\n"
#                          f"Ветер:{wind_speed} m/c \n"
#                          f"Облачность:{cloud_cover} \n"
#                          f"Влажность:{humidity}%")
#         pass
#     except KeyError:
#          await message.answer("Не удалось определить город")


# @dp.message(Command("special_buttons"))
# async def cmd_special_buttons(message: types.Message):
#       kb = [
#             [types.KeyboardButton(text="Запросить контакт", request_contact=True)],
#             [types.KeyboardButton(text="Запросить викторину", request_poll=types.KeyboardButtonPollType(type="quiz"))],
#       ]
#       Keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
#       await message.reply("Выберите действие", reply_markup=Keyboard)

# @dp.message(lambda message: message.text == "Запросить викторину")
# async def send_quiz(message: types.Message):
#       question = "Какой самый большой океан на земле?"
#       options = ["Атлантический", "Индийский","Тихий","Северный Ледовитый"]
#       correct_option_id = 2

#       await bot.send_poll(
#             chat_id=message.chat.id,
#             question=question,
#             options=options,
#             type='quiz',
#             correct_option_id=correct_option_id,
#             is_anonymous=False
#       )
 





# engine = pyttsx3.init()
# engine.setProverty("rate",250)
# engine.setProverty("volume",0.5)
# engine.say("Добро пожаловать, как ваши дела?")
# engine.runAndWait





# @dp.message(Command("game"))
# async def launch_game(message: Message):
#       def run_game():
#             try:
#                   subprocess.Popen(r"c:\Users\itstart\AppData\Local\Google\Chrome\Application\chrome.exe ")
#                   return "Игра запущена!"
#             except FileNotFoundError:
#                 return "Путь к игре не найден. Проверьте путь в коде."

#       loop = asyncio.get_event_loop()
#       response = await loop.run_in_executor(None, run_game)
#       await message.reply(response)          
































# @dp.message(Command("start"))
# async def cmd_name(message: Message):
#     await message.answer("Привет , я тестовый бот")

# @dp.message(Command("info"))
# async def cmd_name(message: Message):
#     await message.reply("У меня есть такие команды - /start, /info")


# btn_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Хоррор")],
#         [KeyboardButton(text="Экшн")],
#         [KeyboardButton(text="Юмор")],
#         [KeyboardButton(text="Фантастика")]
#     ],
#     resize_keyboard=True
#     )
# horror = ["https://hdrezka.ag/films/horror/5300-kladbische-domashnih-zhivotnyh-2-1992.html", "https://hdrezka.ag/films/horror/75599-ritual-2024.html", "https://hdrezka.ag/films/horror/75643-koshmar-na-kladbische-1985.html"]
# action = ["https://hdrezka.ag/films/action/75334-vampir-i-mstitel-2022.html", "https://hdrezka.ag/films/action/75659-sverhzvukovoy-2002.html", "https://hdrezka.ag/cartoons/adventures/75649-korova-kot-i-okean-2006.html"]
# fantastic = ["https://hdrezka.ag/cartoons/fiction/75561-hraniteli-glava-ii-2024.html", "https://hdrezka.ag/films/fiction/75639-antitelo-2002.html", "https://hdrezka.ag/films/fantasy/75619-rokovaya-ekspediciya-2024.html"]
# humor = ["https://www.kinopoisk.ru/film/8124/", "https://www.kinopoisk.ru/series/687595/", "https://www.kinopoisk.ru/film/6039/"]


# @dp.message(Command("films"))
# async def cmd_name(message: Message):
#      await message.answer("Выберите жанр", reply_markup=btn_keyboard)

# @dp.message(lambda message: message.text == "Хорор")
# async def show_horror(message: Message):
#     await message.reply("А вот и не плохой ужастик " + random.choice(horror))
# @dp.message(lambda message: message.text == "Экшн")
# async def show_action(message: Message):
#     await message.reply("А вот и не плохой Экшн " + random.choice(horror))
# @dp.message(lambda message: message.text == "Фантастика")
# async def show_fantastic(message: Message):
#     await message.reply("А вот и не плохая Фантастика " + random.choice(horror))
# @dp.message(lambda message: message.text == "Юмор")
# async def show_humor(message: Message):
#     await message.reply("А вот и не плохой Юмор " + random.choice(horror))



async def main():
      await dp.start_polling(bot)

if __name__=="__main__":
     asyncio.run(main())

