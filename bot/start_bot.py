import telebot
import requests
from telebot import types

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://habr.com/ru/all/')
    btn2 = types.InlineKeyboardButton('custom command', callback_data='test')
    markup.add(btn2)
    markup.add(btn1)
    bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт хабра", reply_markup=markup)


@bot.message_handler(commands=['test'])
def some_action(message):
    print(type(message.from_user.first_name))
    bot.send_message(message.from_user.id, "test")
    response = requests.post('http://127.0.0.1:8000/api/users/', data={
        'telegram_user_id': message.from_user.id,
        'user_first_name': message.from_user.first_name,
    })
    json_data = response.json()
    bot.send_message(message.from_user.id, str(json_data))
    save_message_response = requests.post('http://127.0.0.1:8000/api/messages/', data={
        'telegram_user_id': message.from_user.id,
        'text': message.text,
    })
    send_message_json = save_message_response.json()
    bot.send_message(message.from_user.id, str(send_message_json))

bot.polling(none_stop=True, interval=0)

