import RPi.GPIO as GPIO

# Configuramos la enumeracion de los pines de la rasp
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Creamos el objeto led al cual tendrá los métodos de prender y apagar así como algunos atributos que no atudara a diferencias cada uno de ellos
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

# Generamos los objetos
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

# Simulamos un switch case para prender el led llamando el metodo turnON del objeto
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

# Simulamos un switch case para apagar el led llamando el metodo turnOFF del objeto    
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

# Funcion para conocer el estado de un led (ON/OFF)
def led_state(led, state):
	if state == True:
		return 'led_{} --> ON\n'.format(led)
	else: return 'led_{} --> OFF\n'.format(led)

# Generamos un texto que se mandará como mensaje de la lista de estados de todos los leds
def leds_state_list():
	state_list = led_state(0, led_0.state) + led_state(1, led_1.state) + led_state(2, led_2.state) + led_state(3, led_3.state) + led_state(4, led_4.state) + led_state(5, led_5.state) + led_state(6, led_6.state) + led_state(7, led_7.state) + led_state(8, led_8.state) + led_state(9, led_9.state)
	return state_list