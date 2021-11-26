# Funcionamiento del Bot de Telegram para controlar sistemas del hogar con un Raspberry Pi (Progrmación)
---
<img src="/static/rasp-logo.png" width="150" />
<img src="/static/Telegram-logo.png" width="250" />
<img src="/static/Python-logo.png" width="150" />
<!--
!['Telegram'](Telegram-logo.png "Telegram") 
!['Python'](Python-logo.png "Python")
-->

---
## 1) Creando un bot en telegram
Antes de iniciar, debemos tener Telegram instalado ya sea en tu celular o computadora.

Buscaremos "botFather" (este bot nos permitira crear nuestros propios bots) en la lsita de contactos de la siguiente manera: `@BotFather`

!['Search botFather'](/static/Crear_bot1.png "Search botFather") 

Pulsamos en el botón **iniciar** y lo que nos aparecerá a continuación serán unas breves instrucciones de cómo manejar el bot. Tambien podemos acceder a estos comandos en el icono que se encuentra debajo del chat. Esta lisita de comandos nos permitira crear nuestro propio bot.

!['Search botFather'](/static/Crear_bot2.png "Search botFather") 

Para crear un nuevo bot escribimos el comando `/newbot`. Una vez hecho esto, nos pedirá escribir el nombre de nuestro bot. 
Despúes nos pedirá ponerle al bot un nombre de usuario, y nos obligará a que ese nombre de usuario termine en *bot* ("nombre_usurario"bot).

!['Search botFather'](/static/Crear_bot3.png "Search botFather") 

Finalmente, nos enviara un mensaje en donde se encontrara un **Token** que nos servira para tener accero a la API.

Existen otras opciones para configurar nuestro bot, puedes seguir investigando para que tu bot se vea mejor.

---
## 2) Configuración de la Raspberry PI

Primero, deberas intalar un sistema operativo a tu raspberry y establecer una comunicacion ssh entre la raspberry y tu computadora. Sin embargo como el proposito del documento no es ese, nos saltaremos esa explicación porque suponemos que el lector conoce de estos conceptos, de no ser así, te proporcionamos un tutorial que te ayude a entender mejor estos temas:

*Tutorial:* [*Raspberry Pi, Curso para principiantes*](https://www.youtube.com/watch?v=ra6kNSIB1uA&t=4151s)

Dentro de nuestra raspberry, entraremos a la terminal y actualizaremos el sistema con los siguientes comandos: 
```bash
$ sudo apt-get update
$ sudo apt-get upgrade
```

Una vez se termine de actualizarse, instalaremos los siguientes paquetes de python (no es necesario instalar python porque la raspberry ya lo tiene intalado):
```bash
$ sudo apt-get install python-pip
```

Ahora instalaremos las siguientes librerias: 
```bash
$ sudo pip install telepot
$ sudo pip install requests
$ sudo pip install RPi.GPIO
```

---
## 3) Desarrollo del codigo en python

En esta sección explicaremos paso por paso como programamos el bot para el proyecto, si solo deseas cargar los archivos del proyecto puedes ir a la sección *"Cargar codigo del proyecto"*

Sin más que agregar, comenzamos con la explicación:

Crearemos una carpeta para el proyecto y nos colocamos dentro del él (puede ser cualquier nombre pero por preferencia que tenga que ver con el proyecto):
```bash
$ mkdir telegram_bot
$ cd telegram_bot
```

Generamos los siguientes archivos con el siguiente comando:
```bash
$ touch main.py camara_functions.py weather.py led_functions.py
```
### 3.1) Obtener el clima de cualquier ciudad
Modifiaremos el archivo `weather.py` y definieremos una funcion para obtener el clima con ayuda de OpenWeatherMap que es un servicio en línea, propiedad de OpenWeather Ltd, que proporciona datos meteorológicos globales a través de API, incluidos datos meteorológicos actuales, pronósticos, predicciones inmediatas y datos meteorológicos históricos para cualquier ubicación geográfica. Esta funcion posteriormente sera llamada en el archivo `main.py`. Escribiremos el siguiente codigo en él:

```python
# -*- coding: utf-8 -*-

# Codigo para comunicarnos con la API (openweather) para obtener el clima de una ciudad

import requests     # importamos la libreria para comunicarnos con la API.
import datetime

now = datetime.datetime.now() # Getting date and time...

def date():
   date = str("Date: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year) 
   return date

def time():
   time = str("Time: ") + str(now.hour) + str(":") + str(now.minute) + str(":") + str(now.second)
   return time

def get_info(command):

   # command = /clima 'ciudad'
   city = command[command.index(' ') + 1:]

   # Hacemos la consulta
   url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=53b0ff471d9a8828d27fc13e19fc7482&units=metric".format(city)
   res = requests.get(url)

   # guardamos los datos de la consulta en una variable con estilo json
   data = res.json()

   # Rescatamos los datos que más nos interesan y los guardamos en variables
   temp = data["main"]["temp"]
   vel_viento = data["wind"]["speed"]
   latitud = data["coord"]["lat"]
   longitud = data["coord"]["lon"]
   descripcion = data["weather"][0]["description"]
   presion = data["main"]["pressure"]
   humedad = data["main"]["humidity"]

   # Creamos un string donde guardaremos todos los datos para que el bot envie ese mensaje
   info = " Temperatura: {0} \n Velocidad del viento: {1} m/s \n Presion: {2} hPa \n Humedad = {3}% \n Latitud: {4} \n Longitud: {5} \n Descripcion: {6} \n".format(temp, vel_viento, presion, humedad, latitud, longitud, descripcion)

   return info
```
### 3.2) codigo de para las funciones de la cámara
Modifiaremos el archivo `camara_functions.py` y definieremos en él unas funciones que nos permitan grabar un video o tomar una foto, los cuales serán guardados en un directoria para que posteriormente el bot tenga acceso a ellos. Entonces, en el archivo antes mencionado escribiremos el siguiente código:
```python
from picamera import PiCamera
from time import sleep
from signal import pause

# Puedes modificar la ruta donde se guardaran tus archivos, preferentemente que sea dentro de la carpeta donde estas desarrollando el proyecto
ruta_destino = '/home/pi/Proyectos/projectTelegramBot_v2/media/'

camara = PiCamera()

def tomar_foto():
   camara.start_preview()
   sleep(3)
   camara.capture(ruta_destino + 'captura_rasp.jpg')
   camara.stop_preview()

def grabar_video():
   camara.start_preview()
   sleep(3)
   camara.start_recording(ruta_destino + 'video_rasp.h264')
   sleep(5)
   camara.stop_recording()
   camara.stop_preview()
```

### 3.3) Codigo para las funciones de los leds
Modificaremos el archivo `leds_functions.py`, este codigo crearemos una clase al cual llamaremos leds y definiremos sus metodos (ON/OFF):
```python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class Led:
    def __init__(self, pin):
        self.pin = pin
        self.state = False
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, self.state)

    def turnON(self):
        self.state = True
        GPIO.output(self.pin, self.state)
        print('Pin {} Encendido'.format(str(self.pin)))

    def turnOFF(self):
        self.state = False
        GPIO.output(self.pin, self.state)
        print('Pin {} Apagado'.format(str(self.pin)))

# Creamos nuestros objetos (leds)
led_0 = Led(11)
led_1 = Led(13)
led_2 = Led(15)
led_3 = Led(16)
led_4 = Led(18)
led_5 = Led(22)
led_6 = Led(29)
led_7 = Led(31)
led_8 = Led(36)
led_9 = Led(37)

# Simulamos un switch case para que el usuario escoga cualquier led y este ejecute el metodo de prender el led
def turn_on(argument):
    switcher = {
        0:led_0.turnON,
        1:led_1.turnON,
        2:led_2.turnON,
        3:led_3.turnON,
        4:led_4.turnON,
        5:led_5.turnON,
        6:led_6.turnON,
        7:led_7.turnON,
        8:led_8.turnON,
        9:led_9.turnON,
    }

    return switcher.get(argument, "Defalt")

# Simulamos un switch case para que el usuario escoga cualquier led y este ejecute el metodo de apagar el led    
def turn_off(argument):
    switcher = {
        0:led_0.turnOFF,
        1:led_1.turnOFF,
        2:led_2.turnOFF,
        3:led_3.turnOFF,
        4:led_4.turnOFF,
        5:led_5.turnOFF,
        6:led_6.turnOFF,
        7:led_7.turnOFF,
        8:led_8.turnOFF,
        9:led_9.turnOFF,
    }

    return switcher.get(argument, "Defalt")

# Funciones para conocer los estados de los led para posteriormente el usuario puedo verlos en el chat
def led_state(led, state):
	if state == True:
		return 'led_{} --> Encendido\n'.format(led)
	else: return 'led_{} --> Apagado\n'.format(led)

def leds_state_list():
	state_list = led_state(0, led_0.state) + led_state(1, led_1.state) + led_state(2, led_2.state) + led_state(3, led_3.state) + led_state(4, led_4.state) + led_state(5, led_5.state) + led_state(6, led_6.state) + led_state(7, led_7.state) + led_state(8, led_8.state) + led_state(9, led_9.state)
	return state_list
``` 

### 3.4) Comunicacion con el bot
Finalmente, en el archivo `main.py` colocaremos el codigo que nos permite interactuar con el bot por medio de telegram, este archivo llamara a las otras funciones declaradas anteriormente:
```python
# -*- coding: utf-8 -*-

import telepot                          
from telepot.loop import MessageLoop    
from time import sleep

import camara_functions as camara
import weather
import leds_functions as light


def handle(msg):
    # Obtenemos informacion del mensaje
    chat_id = msg['chat']['id']     
    command = msg['text']           

    print ('Received:')
    print(command)

    # Comparamos el mensaje recibido y ejecutamos cierta funcion segun sea el caso
    if command == '/hi':
        bot.sendMessage (chat_id, "Hola nena UwU  <3")

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

    elif command == '/photo':
        try:
            bot.sendMessage(chat_id, str("Taking photo ..."))
            camara.take_foto()
            bot.sendMessage(chat_id, str("Ready!!!"))
            bot.sendPhoto(chat_id, open('/home/pi/Proyectos/projectTelegramBot_v2/media/captura_rasp.jpg', 'rb'))
        except:
            bot.sendMessage(chat_id, str('Error, intentelo más tarde :c'))

    elif command == '/video':
        try:
            bot.sendMessage(chat_id, str("recording ..."))
            camara.record_video()
            bot.sendMessage(chat_id, str("Ready!!!"))
            bot.sendVideo(chat_id, open('/home/pi/Proyectos/projectTelegramBot_v2/media/video_rasp.h264', 'rb'))
        except:
            bot.sendMessage(chat_id, str('Error, intentelo más tarde :c'))

# Insert your telegram token below
bot = telepot.Bot('######################')
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

# Keep the program running.
while 1:
    sleep(10)
```

### *Cargar codigo del proyecto*
Si solo deseas cargar los archivos del proyecto directamente, puedes obtenerlos mediante el siguiente comando:
```bash
$ git clone https://github.com/PakoMtzR/telegram_bot.git
```

En el archivo `main.py` introducimos el token de nuestro bot:
```python
bot = telepot.Bot('Bot Token')
```

Acto seguido, ejecutamos el bot de Python:
```bash
$ python main.py
```
Listo, ahora puedes saltarte esta seccion para ir a la conexión de los componentes.

---
##### *Nota: Revisa el manual de usuario adjunto para conocer acerca de las conexiones, mantenimiento y operación del producto.*











