# Bot de Telegram para controlar sistemas del hogar con un Raspberry Pi 
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
$ touch main.py camara_funciones.py clima_api.py lights.py
```
### 3.1) Obtener el clima de cualquier ciudad
Modifiaremos el archivo `clima_api.py` y definieremos una funcion para obtener el clima con ayuda de OpenWeatherMap que es un servicio en línea, propiedad de OpenWeather Ltd, que proporciona datos meteorológicos globales a través de API, incluidos datos meteorológicos actuales, pronósticos, predicciones inmediatas y datos meteorológicos históricos para cualquier ubicación geográfica. Esta funcion posteriormente sera llamada en el archivo `main.py`. Escribiremos el siguiente codigo en él:

```python
# Codigo para comunicarnos con la API (openweather) para obtener el clima de una ciudad

import requests     # importamos requests para comunicarnos con la API.

def obtener_info(command):

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
Modifiaremos el archivo `clima_api.py` y definieremos en él unas funciones que nos permitan grabar un video o tomar una foto, los cuales serán guardados en un directoria para que posteriormente el bot tenga acceso a ellos. Entonces, en el archivo antes mencionado escribiremos el siguiente código:
```python
from picamera import PiCamera
from time import sleep
from signal import pause
# import os
# import datetime as dt

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
## 4) Conexión de hardware a la raspberry

*Fuentes:*
* https://technetters.com/crea-un-bot-de-telegram-raspberry-pi-python/
* https://www.flopy.es/crea-un-bot-de-telegram-para-tu-raspberry-ordenale-cosas-y-habla-con-ella-a-distancia/
---













