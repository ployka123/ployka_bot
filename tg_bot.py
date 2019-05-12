import telebot
import pyowm

from telebot import apihelper
apihelper.proxy = { "https": "socks5://111.223.75.178:8888"}

owm = pyowm.OWM('6e0df22df60df943f1c84578333a0dc5', language = "ru")
bot = telebot.TeleBot("863915954:AAG9GXiCpEq0zN9ax7JmfsMJvu3LedrkL1A")

@bot.message_handler(content_types=['text'])
def send_welcome(message):

    observation = owm.weather_at_place( message.text )
    w = observation.get_weather()
    temp = w.get_temperature("celsius")["temp"]
    humidity = w.get_humidity()

    def direction_wind():

        if  w.get_wind()['deg'] <= 22.5:
            return 'северный'

        if w.get_wind()['deg'] > 337.5:
            return 'северный'

        if 22.5 < w.get_wind()['deg'] <= 67.5:
            return 'северо-восточный'

        if 67.5 < w.get_wind()['deg'] <= 112.5:
            return 'восточный'

        if 112.5 < w.get_wind()['deg'] <= 157.5:
            return 'юго-восточный'

        if 157.5 < w.get_wind()['deg'] <= 202.5:
            return 'южный'

        if 202.5 < w.get_wind()['deg'] <= 247.5:
            return 'юго-западный'

        if 247.5 < w.get_wind()['deg'] <= 292.5:
            return 'западный'

        if 292.5 < w.get_wind()['deg'] <= 337.5:
            return 'северо-западный' # Направление ветра

    def speed_wind():

        if w.get_wind()["speed"] <= 0.5:
            return "штиль"

        if w.get_wind()["speed"] <= 1.7:
            return "тихий"

        if w.get_wind()["speed"] <= 3.3:
            return "легкий"

        if w.get_wind()["speed"] <= 5.2:
            return "слабый"

        if w.get_wind()["speed"] <= 7.4:
            return "умеренный"

        if w.get_wind()["speed"] <= 9.8:
            return "свежий"

        if w.get_wind()["speed"] <= 12.4:
            return "сильный"

        if w.get_wind()["speed"] <= 15.2:
            return "крепкий"

        if w.get_wind()["speed"] <= 18.2:
            return "очень крепкий"

        if w.get_wind()["speed"] <= 21.5:
            return "шторм"

        if w.get_wind()["speed"] <= 25.1:
            return "сильный шторм"

        if w.get_wind()["speed"] <= 29:
            return "жесткий шторм"

        if w.get_wind()["speed"] > 29:
            return "ураган" # Скорость ветра

    def advice():
        if temp > 30 and w.get_wind()["speed"] <= 5.2:
            return "Жарко пздц, сиди под кондиционером"

        if temp > 30 and w.get_wind()["speed"] <=12.4:
            return "Жара, но ветер способен спасти тебе жизнь"

        if temp > 30 and w.get_wind()["speed"] <= 29:
            return "Там конечно жарко, но нахуй этот ветер"

        if temp > 25 and w.get_wind()["speed"] <= 5.2:
            return "Там очень жарко, сиди дома мудак"

        if temp > 25 and w.get_wind()["speed"] <=12.4:
            return "Это лучшая погода для гулянок"

        if temp > 25 and w.get_wind()["speed"] <= 29:
            return "Погода хорошая, ветер хуёвый"

        if temp > 20 and w.get_wind()["speed"] <= 5.2:
            return "И почему ты до сих пор дома?"

        if temp > 20 and w.get_wind()["speed"] <=12.4:
            return "Бегом на улицу"

        if temp > 20 and w.get_wind()["speed"] <= 29:
            return "Всё хорошо, только очень ветренно"

        if temp > 15 and w.get_wind()["speed"] <= 5.2:
            return "Погода хорошая, но лучше идти в кофте"

        if temp > 15 and w.get_wind()["speed"] <=12.4:
            return "Погода вроде ничего"

        if temp > 15 and w.get_wind()["speed"] <= 29:
            return "Погода так себе, да ещё и сильный ветер"

        if temp > 10 and w.get_wind()["speed"] <= 5.2:
            return "Оденься!"

        if temp > 10 and w.get_wind()["speed"] <=12.4:
            return "Одень куртку, окк"

        if temp > 10 and w.get_wind()["speed"] <= 29:
            return "Бля, прохладно и ветер"

        if temp > 5 and w.get_wind()["speed"] <= 5.2:
            return "Одевайся потеплее"

        if temp > 5 and w.get_wind()["speed"] <=12.4:
            return "Одень куртку, там ветер"

        if temp > 5 and w.get_wind()["speed"] <= 29:
            return "Прохлажно и сильный ветер, сиди дома"

        if temp > 0 and w.get_wind()["speed"] <= 5.2:
            return "Сиди дома"

        if temp > 0 and w.get_wind()["speed"] <=12.4:
            return "Дома, дом и только дом"

        if temp > 0 and w.get_wind()["speed"] <= 29:
            return "Лучшая погода, чтобы остаться дома"

        if temp <= 0 and w.get_wind()["speed"]:
            return "Сиди дома, нахуй эту улицу" # Совет

    def wind():

        if w.get_wind()["speed"] <= 0.5:
            return ""

        if w.get_wind()["speed"] <= 3.2:
            return  "ветерок"

        if w.get_wind()["speed"] < 21.5:
            return  "ветер"

        if w.get_wind()["speed"] >= 21.5:
            return  "" # Ветер/ветерок

    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
    answer += "Температура в районе " + str(temp) + " ℃ " + "\n"
    answer += "В данный момент на улице " + speed_wind() + " " + direction_wind() + " " + wind() + "\n"
    answer += "Влажность воздуха примерно " + str(humidity) + " % " + "\n"
    answer += str(advice())
    bot.send_message(message.chat.id, answer)
bot.polling( none_stop = True)
