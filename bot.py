import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Понедельник")
    btn2 = types.KeyboardButton("Вторник")
    btn3 = types.KeyboardButton("Среда")
    btn4 = types.KeyboardButton("Четверг")
    btn5 = types.KeyboardButton("Пятница")
    btn6 = types.KeyboardButton("Суббота")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! На какой день недели узнать расписание?".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Понедельник"):
        bot.send_message(message.chat.id, text="1 пара: Деловой и технический иностранный язык")
    elif(message.text == "Вторник"):
        bot.send_message(message.chat.id, text="3-4 пары: Основы разрботки ПО-В")
    elif(message.text == "Среда"):
        bot.send_message(message.chat.id, "1 пара: Физическая культура\n(нечёт)2 пара: Правовое и экологическе обеспечение")
    elif message.text == "Четверг":
        bot.send_message(message.chat.id, text="(чёт)1 пара: Правовое и экологоическое обеспечение\n(нечёт)1 пара: Эргономика")
    elif (message.text == "Пятница"):
        bot.send_message(message.chat.id, text="1 пара: Физическая культура\n(нечёт)1-2 пары: Основы тестирования ПО\n(чёт)1-2 пары: Проектирование ИС")
    elif (message.text == "Суббота"):
        bot.send_message(message.chat.id, text="(нечёт)1-4 пары: Языки программирования высокого уровня\n(чёт)1-2 пары: Технологии организации НИР")
    else:
        bot.send_message(message.chat.id, text="Такую команду не знаю!")

bot.polling(none_stop=True)
