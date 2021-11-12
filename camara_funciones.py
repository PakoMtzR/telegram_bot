from picamera import PiCamera
from time import sleep
# import os
# import datetime as dt
from signal import pause

ruta_destino = '/home/pi/Proyectos/projectTelegramBot_v2/media/'
camara = PiCamera()


def tomar_foto():
   camara.start_preview()
   sleep(3)
   camara.capture(ruta_destino + 'captura_rasp.jpg')
   camara.stop_preview()

def grabar_video():
   # nombre_video = os.path.join(destino,dt.datetime.now().strftime('%Y-%m-%d_%H.%M.%S.h264'))
   camara.start_preview()
   sleep(3)
   camara.start_recording(ruta_destino + 'video_rasp.h264')
   sleep(5)
   camara.stop_recording()
   camara.stop_preview()

