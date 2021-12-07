# -*- coding: utf-8 -*-

import telepot                          # Importing the telepot library
from telepot.loop import MessageLoop    # Library function to communicate with telegram bot
#import datetime                         # Importing the datetime library
from time import sleep
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
import clima_api as clima

import light_test as light


def handle(msg):
    #content_type, chat_type, chat_id = telepot.glance(msg)
    chat_id = msg['chat']['id']
    command = msg['text']
    #print(content_type, chat_type, chat_id)
    print(msg, ' \n')
    # buttons = [[KeyboardButton(text = 'randomImageText')], [KeyboardButton(text = 'randomPeopleText')]]
    bot.sendMessage(chat_id = msg['chat']['id'], text = command, reply_markup=ReplyKeyboardMarkup([KeyboardButton('randomImageText')]))


# Insert your telegram token below
bot = telepot.Bot('1973126486:AAFjyJsMHAM8LhcXUTexWUKREtbZJnu6Noc')
print(bot.getMe())


# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

# Keep the program running.
while 1:
    sleep(10)
