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
