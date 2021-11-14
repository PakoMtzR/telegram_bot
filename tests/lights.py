import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Definimos los pines para cada led:
led_0 = 11
led_1 = 13
led_2 = 15
led_3 = 16
led_4 = 18
led_5 = 22
led_6 = 29
led_7 = 31
led_8 = 36
led_9 = 10

# Declaramos los pines como salidas
GPIO.setup(led_0, GPIO.OUT)
GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(led_3, GPIO.OUT)
GPIO.setup(led_4, GPIO.OUT)
GPIO.setup(led_5, GPIO.OUT)
GPIO.setup(led_6, GPIO.OUT)
GPIO.setup(led_7, GPIO.OUT)
GPIO.setup(led_8, GPIO.OUT)
GPIO.setup(led_9, GPIO.OUT)


# command = /TurnON led_01
# command = /TurnOFF led_01
'''
def turnON_light(command):
    led = command[command.index(' ') + 1:]
    GPIO.output(led, True)

def turnOFF_light(command):
    led = command[command.index(' ') + 1:]
    GPIO.output(led, False)
'''    
