# -*- coding: utf-8 -*-

import serial
import telepot                          
from telepot.loop import MessageLoop    
from time import sleep
import asyncio

#import camara_functions as camara
import weather
import leds_functions as light

arduino = serial.Serial('/dev/ttyACM0', 9600)
arduino.flush()

async def arduinoSerial():
    while True:
        if arduino.in_waiting > 0:
            line = str(arduino.readline())      #.decode('uft-8').rstrip()
            timbre = line[3]
            gas = line[5]
            print(line)
            #print(timbre)
            #print(gas)
            if timbre == '1': bot.sendMessage(1597500632, '[ALERTA]: Han tocado el timbre')
            if gas == '1': bot.sendMessage(1597500632, '[ALERTA]: Fuga de gas!!!')

def handle(msg):
    # Obtenemos informacion del mensaje
    chat_id = msg['chat']['id']     
    command = msg['text']           
    print(chat_id) 
    print ('Received:')
    print(command)
    
    # Comparamos el mensaje recibido y ejecutamos cierta funcion segun sea el caso
    if command == '/hi':
        bot.sendMessage(chat_id, "Hola nena UwU  <3")

    elif command == '/time':
        time = weather.time()
        bot.sendMessage(chat_id, time)

    elif command == '/date':
        date = weather.date()
        bot.sendMessage(chat_id, date)

    elif command.startswith('/turn_on '):
        try:
            led = int(command[command.index(' ') + 1:])
            output = light.turn_on(led)
            output()
            bot.sendMessage(chat_id, 'Led {} encendido'.format(str(led)))
        except:
            bot.sendMessage(chat_id, 'Error: Intentelo más tarde')
    
    elif command.startswith('/turn_off '):
        try:
            led = int(command[command.index(' ') + 1:])
            output = light.turn_off(led)
            output()
            bot.sendMessage(chat_id, 'Led {} apagado'.format(str(led)))
        except:
            bot.sendMessage(chat_id, 'Error: Intentelo más tarde')

    elif command.startswith('/weather '):
        try:
            info = weather.get_info(command)
            bot.sendMessage(chat_id, str(info))
        except:
            bot.sendMessage(chat_id, str('Error, intentelo más tarde :c'))
    
    elif command == '/state_list':
        leds_states = light.leds_state_list()
        bot.sendMessage(chat_id, leds_states)
'''
    elif command == '/photo':
        try:
            bot.sendMessage(chat_id, str("Taking photo ..."))
            camara.take_foto()
            bot.sendMessage(chat_id, str("Ready!!!"))
            bot.sendPhoto(chat_id, open('/home/pi/Proyectos/projectTelegramBot_v2/media/captura_rasp.jpg', 'rb'))
        except:
            bot.sendMessage(chat_id, str('Error, intentelo más tarde :c'))
    '''
'''    
elif command == '/video':
        try:
            bot.sendMessage(chat_id, str("recording ..."))
            camara.record_video()
            bot.sendMessage(chat_id, str("Ready!!!"))
            bot.sendVideo(chat_id, open('/home/pi/Proyectos/projectTelegramBot_v2/media/video_rasp.h264', 'rb'))
        except:
            bot.sendMessage(chat_id, str('Error, intentelo más tarde :c'))
    '''
# Insert your telegram token below
bot = telepot.Bot('1973126486:AAFjyJsMHAM8LhcXUTexWUKREtbZJnu6Noc')
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')
asyncio.run(arduinoSerial())

# Keep the program running.
while 1:
    sleep(10)
