from constants import TOKEN
import telebot
import requests
import messages
from telebot import types

bot = telebot.TeleBot(TOKEN)

markup_s = types.ReplyKeyboardMarkup(row_width=2)
markup_f = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('Толе би')
itembtn2 = types.KeyboardButton('Абылай хана')
itembtn3 = types.KeyboardButton('Панфилова')
itembtn4 = types.KeyboardButton('Казыбек би')
itembtn5 = types.KeyboardButton('1')
itembtn6 = types.KeyboardButton('2')
itembtn7 = types.KeyboardButton('3')
itembtn8 = types.KeyboardButton('4')
markup_s.row(itembtn1, itembtn4)
markup_s.row(itembtn2, itembtn3)
markup_f.row(itembtn5, itembtn6)
markup_f.row(itembtn7, itembtn8)

counter = 2

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, messages.HELLO, reply_markup=markup_s)


@bot.message_handler(regexp='Толе би')
def send_floors(message):
    bot.send_message(message.chat.id, messages.FLOOR, reply_markup=markup_f)
    open('saved_messages.txt', 'a').write('\n' + str(message.from_user.username) + ' || ' + message.text + ' ')


@bot.message_handler(regexp='Казыбек би')
def send_floors(message):
    bot.send_message(message.chat.id, messages.FLOOR, reply_markup=markup_f)
    open('saved_messages.txt', 'a').write('\n' + str(message.from_user.username) + ' || ' + message.text + ' ')


@bot.message_handler(regexp='Панфилова')
def send_floors(message):
    bot.send_message(message.chat.id, messages.FLOOR, reply_markup=markup_f)
    open('saved_messages.txt', 'a').write('\n' + str(message.from_user.username) + ' || ' + message.text + ' ')


@bot.message_handler(regexp='Абылай хана')
def send_floors(message):
    bot.send_message(message.chat.id, messages.FLOOR, reply_markup=markup_f)
    open('saved_messages.txt', 'a').write('\n' + str(message.from_user.username) + ' || ' + message.text + ' ')

@bot.message_handler(regexp='1')
def save_floor(message):
    bot.send_message(message.chat.id, messages.WHERE, markup_s)
    open('saved_messages.txt', 'a').write(message.text + ' || ')

@bot.message_handler(regexp='2')
def save_floor(message):
    open('saved_messages.txt', 'a').write(message.text + ' || ')

@bot.message_handler(regexp='3')
def save_floor(message):
    open('saved_messages.txt', 'a').write(message.text + ' || ')

@bot.message_handler(regexp='4')
def save_floor(message):
    open('saved_messages.txt', 'a').write(message.text + ' || ')

if __name__ == '__main__':
    print('Starting bot...')
    bot.polling()