# -*- coding: utf-8 -*-

import telepot                          # Importing the telepot library
from telepot.loop import MessageLoop    # Library function to communicate with telegram bot
#import datetime                         # Importing the datetime library
from time import sleep

import clima_api as clima

import light_test as light


def handle(msg):
    #content_type, chat_type, chat_id = telepot.glance(msg)
    chat_id = msg['chat']['id']
    command = msg['text']
    #print(content_type, chat_type, chat_id)

    #if content_type == 'text':
        #command = msg['text']
    if command.startswith('/turn_on '):
        try:
            led = int(command[command.index(' ') + 1:])
            output = light.turn_on(led)
            output()
            bot.sendMessage(chat_id, 'Led {} encendido'.format(str(led)))
        except:
            bot.sendMessage(chat_id, 'Error: Intentelo más tarde')
    
    if command.startswith('/turn_off '):
        try:
            led = int(command[command.index(' ') + 1:])
            output = light.turn_off(led)
            output()
            bot.sendMessage(chat_id, 'Led {} apagado'.format(str(led)))
        except:
            bot.sendMessage(chat_id, 'Error: Intentelo más tarde')
    '''
    print(msg)
    chat_id = msg['chat']['id']
    command = msg['text']

    #bot.sendMessage(chat_id, str(command))
    print('Received: ' + str(command))
    '''

# Insert your telegram token below
bot = telepot.Bot('1973126486:AAFjyJsMHAM8LhcXUTexWUKREtbZJnu6Noc')
print(bot.getMe())


# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

# Keep the program running.
while 1:
    sleep(10)
