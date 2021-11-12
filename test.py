import telepot                          # Importing the telepot library
from telepot.loop import MessageLoop    # Library function to communicate with telegram bot
#import datetime                         # Importing the datetime library
from time import sleep

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        #return msg['text']
        bot.sendMessage(chat_id, msg['text'])
    
    #print(msg)
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
