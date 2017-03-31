#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import paramiko
import time
from random import choice
import string
import telebot


#login = sys.argv[1]
token = '363953390:AAHqQeLssqkC_aQ2bmUjl_xnfeltpstw-4o'
bot = telebot.TeleBot(token)
chat_id = -217393923
my_id = 173423412
#sudopass = ''

@bot.message_handler(commands=['start'])
def send_welcome(message):
   bot.reply_to(message, "Привет! Используй команду /wifi, чтобы создать пользователя")

@bot.message_handler(commands=['password'])
def get_password(message):
   bot.reply_to(message, "Введи свой пароль")
   @bot.message_handler(content_types=["text"])
   def sudopass(message):
      global sudopass
      sudopass = message.text
      bot.reply_to(message, "Ok!")

@bot.message_handler(commands=['wifi'])
def wifiuser(message):
   bot.reply_to(message, "Введи имя пользователя")
   @bot.message_handler(content_types=["text"])
   def prin(message):
      try:
         if message.chat.id == my_id:
            adduser(str(message.text))
         else:
            bot.send_message(my_id,'Извини, но у тебя нет на это прав')
      except UnicodeEncodeError:
         bot.send_message(my_id,'Пожалуйста, используй латиницу')




def adduser(x):
   host = '172.17.2.104'
   user = 'v.korol'
   sudopass = 'loop7Meg\n'
   port = 22
   password = ''.join(choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(10))
   client = paramiko.SSHClient()
   client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   client.connect(hostname=host, username=user, port=port, key_filename='/root/.ssh/id_rsa')
   stdin, stdout, stderr = client.exec_command('sudo chown v.korol:v.korol /etc/freeradius/users', get_pty=True)
   stdin.write(sudopass)
   stdin.flush()
   time.sleep(2)
   stdin, stdout, stderr = client.exec_command(r'echo "%s Cleartext-Password :=  \"%s\""  >> /etc/freeradius/users' % (x, password))
   stdin, stdout, stderr = client.exec_command('sudo chown root:root /etc/freeradius/users', get_pty=True)
   stdin.write(sudopass)
   stdin.flush()
   stdin, stdout, stderr = client.exec_command('sudo /etc/init.d/freeradius restart', get_pty=True)
   stdin.write(sudopass)
   stdin.flush()
   client.close()
   bot.send_message(my_id, 'пользователь: %s\nпароль: %s' % (x, password))
#   print('user:%s\npassword:%s' % (x, password))

if __name__ == '__main__':
     bot.polling(none_stop=True)


#adduser(Y)
