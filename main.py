from constants import TOKEN
import telebot
import requests
import messages

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome = bot.send_message(message.chat.id, messages.HELLO)
    note = bot.send_message(message.chat.id, messages.PLACES)
    bot.register_next_step_handler(note, savee)

def savee(message):
	location = message.text
	open('saved_messages.txt', 'a').write('\n' + str(message.from_user.username) + ' || ' + location + ' || ')

@bot.message_handler(content_types=['text'])
def send_next_msg(message):
    msg = bot.send_message(message.chat.id, messages.WHERE)
    bot.register_next_step_handler(msg, saveee)

def saveee(message):
    location = message.text
    open('saved_messages.txt', 'a').write(location + ' || ')

@bot.message_handler(content_types=['text'])
def send_way(message):
    with open('saved_messages.txt', "r") as f1:
        current_user = f1.readlines()[-1].split('||')
    fromm = current_user[2]
    to = current_user[1]
    if fromm == 'тб 1' and to == 'аб 2':
        bot.send_message(message.chat.id, messages.TB1AB2)


if __name__ == '__main__':
    print('Starting bot...')
    bot.polling()
