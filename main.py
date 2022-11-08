import telebot
import requests

from config import weather_token

bot = telebot.TeleBot('5552828705:AAFLYXRrfMTUX7NUPMNZnehUERZLGRlqfXc')

@bot.message_handler(commands=['start'])

def start(message):
    mess = f"""Hello, {message.from_user.first_name}!
If you want to know the weather by your coordinates, enter latitude and longitude through space.
"""
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()

def get_user_text(message):
    a = message.text.split(' ')

    get_weather(a[0], a[1], weather_token, message)
    

def get_weather(lat, lon, weather_token, message):
    weather = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_token}&units=metric"
        )
    data = weather.json()


    bot.send_message(message.chat.id, f"""* Temperature: {data["main"]["temp"]}°
* Humidity: {data["main"]["humidity"]}%
* Wind speed: {data["wind"]["speed"]}m/s
* Cloudiness: {data['clouds']['all']}%
    """)


bot.polling(none_stop=True)