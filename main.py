import telepot                          # Importing the telepot library
from telepot.loop import MessageLoop    # Library function to communicate with telegram bot
import datetime                         # Importing the datetime library
from time import sleep

#import camara_funciones as camara
import clima_api as clima
import lights



now = datetime.datetime.now() # Getting date and time...


'''
GPIO.setmode(GPIO.BOARD)

# Definimos los pines para cada led:
led_01 = 11
led_02 = 13
led_03 = 15
led_04 = 16
led_05 = 18
led_06 = 22
led_07 = 29
led_08 = 31
led_09 = 36
led_10 = 10
# Declaramos los pines como salidas
GPIO.setup(led_01, GPIO.OUT)
GPIO.setup(led_02, GPIO.OUT)
GPIO.setup(led_03, GPIO.OUT)
GPIO.setup(led_04, GPIO.OUT)
GPIO.setup(led_05, GPIO.OUT)
GPIO.setup(led_06, GPIO.OUT)
GPIO.setup(led_07, GPIO.OUT)
GPIO.setup(led_08, GPIO.OUT)
GPIO.setup(led_09, GPIO.OUT)
GPIO.setup(led_10, GPIO.OUT)
'''


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
            bot.sendMessage(chat_id, str("Taking photo ..."))
            camara.tomar_foto()
            bot.sendMessage(chat_id, str("Ready!!!"))
            bot.sendPhoto(chat_id, open('/home/pi/Proyectos/projectTelegramBot_v2/media/captura_rasp.jpg', 'rb'))
        except:
            bot.sendMessage(chat_id, str('Error, intentelo más tarde :c'))

    elif command == '/video':
        try:
            bot.sendMessage(chat_id, str("recording ..."))
            camara.grabar_video()
            bot.sendMessage(chat_id, str("Ready!!!"))
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
