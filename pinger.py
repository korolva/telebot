#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import telebot
import sys

token = ''
bot = telebot.TeleBot(token)
chat_id = -217393923
downlist = []

while True:
#   sys.exit()
   hostlist = open('hostlist.txt', 'r')
   for host in hostlist.readlines():
      response = os.system("ping -c 3 " + host.strip() + "> /dev/null 2>&1")
      if response == 0:
         if host.strip() in downlist:
            downlist.remove(host.strip())
            bot.send_message(chat_id, 'Ура! ' + host.strip() + ' снова доступен!')
      elif host.strip() not in downlist:
         downlist.append(host.strip())
         bot.send_message(chat_id, 'Похоже, что ' + host.strip() + ' не доступен')

