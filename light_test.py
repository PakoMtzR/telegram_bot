import RPi.GPIO as GPIO
from time import sleep

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


def led_state(led, state):
	if state == True:
		return 'led_{} --> Encendido\n'.format(led)
	else: return 'led_{} --> Apagado\n'.format(led)

def leds_state_list():
	state_list = led_state(0, led_0.state) + led_state(1, led_1.state) + led_state(2, led_2.state) + led_state(3, led_3.state) + led_state(4, led_4.state)
	return state_list

'''
led_0.turnON()
sleep(5)
led_0.turnOFF()
-------------------------

output = turn_on(0)
output()
sleep(2)
output = turn_off(0)
output()

'''
