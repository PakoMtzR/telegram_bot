import telepot                          # Importing the telepot library
from telepot.loop import MessageLoop    # Library function to communicate with telegram bot
#import datetime                         # Importing the datetime library
from time import sleep

#import camara_funciones as camara
#import clima_api as clima
#import lights

#now = datetime.datetime.now() # Getting date and time...

'''
def sumar(chat_id):
    bot.sendMessage(chat_id, str('Ingrese a = '))
'''

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

"""
def handle(msg):
    chat_id = msg['chat']['id']     # Receiving the message from telegram
    command = msg['text']           # Getting text from the message

    print ('Received:')
    print(command)

    # Comparing the incoming message to send a reply according to it
    if command == '/hi':
        bot.sendMessage (chat_id, str("Hola nena UwU  <3"))

    elif command == '/time':
        bot.sendMessage(chat_id, str("Time: ") + str(now.hour) + str(":") + str(now.minute) + str(":") + str(now.second))

    elif command == '/date':
        bot.sendMessage(chat_id, str("Date: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))

    elif command.startswith('/turn_on '):
        try:
            led = command[command.index(' ') + 1:]
            GPIO.output(led, True)
            bot.sendMessage(chat_id, str("Led is ON"))
        except:
            bot.sendMessage(chat_id, str("Error, intentelo más tarde"))

    elif command.startswith('/turn_off '):
        try:
            led = command[command.index(' ') + 1:]
            GPIO.output(led, True)
            bot.sendMessage(chat_id, str("Led is OFF"))
        except:
            bot.sendMessage(chat_id, str("Error, intentelo más tarde"))


            bot.sendMessage(chat_id, str('Error, intentelo más tarde :c'))

    elif command.startswith('/weather '):
        try:
            info = clima.obtener_info(command)
            bot.sendMessage(chat_id, str(info))
        except:
            bot.sendMessage(chat_id, str('Error, intentelo más tarde :c'))
    
    '''
    elif command == '/photo':
        try:
            camara.tomar_foto()
            bot.sendChatAction(chat_id, 'cargando foto...')
            bot.sendPhoto(chat_id, open('/home/pi/Proyectos/projectTelegramBot_v2/media/captura_rasp.jpg', 'rb'))
        except:
            bot.sendMessage(chat_id, str('Error, intentelo más tarde :c'))

    elif command == '/video':
        try:
            camara.grabar_video() 
            bot.sendChatAction(chat_id, 'cargando video...')
            bot.sendPhoto(chat_id, open('/home/pi/Proyectos/projectTelegramBot_v2/media/video_rasp.h264', 'rb'))
        except:
            bot.sendMessage(chat_id, str('Error, intentelo más tarde :c'))
    '''

#if __name__ == "__main__":
# Insert your telegram token below
bot = telepot.Bot('1973126486:AAFjyJsMHAM8LhcXUTexWUKREtbZJnu6Noc')
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

while 1:
    sleep(10)
"""
