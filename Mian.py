#_*_ coding: utf-8 _*_

import telebot

import config
from config import name,number,points

from DataBasssee import mySQL
import DataBasssee

name =False

regs = False
reg_stady = 0

bot = telebot.TeleBot(config.token)

# @bot.message_handler(commands=['start'])
# def firstMessage(message):
#     if db_worker.insert_message(message.chat.id) is True:
#         bot.send_message(message.chat.id, "Успешно!")

@bot.message_handler(commands=['reg'])
def registrations(message):
    global regs
    regs = True
    bot.send_message(message.chat.id, "Введите номер телефона и имя")

@bot.message_handler(commands=["text"])
def dispather(message):
    if (reg is True):
        global reg_stady
        global regs
        reg_stady += 1
        if(reg_stady == 1):
            if message == "+7999":
                number = message
                bot.send_message(message.chat.id, "Теперь имя")
                reg_stady+=1
            else:bot.send_message("Такой формат не поддерживается")
        if(reg_stady == 2):
            name = message
            bot.send_message(message.chat.id, "Введите количество баллов")
        if(reg_stady == 3):
            points = int(message)
            bot.send_message(message.chat.id,"Заносим в базу данных")
            db_worker = mySQL(config.database_neme)
            if db_worker.registration(number,name,points) is True:
                bot.send_message(message.chat.id, "Успешно")
            else:bot.send_message(message.chat.id, "Ошибка")
            reg_stady = 0
            reg = False
if __name__ == '__main__':
    bot.polling(none_stop=True)
