import RPi.GPIO as GPIO

import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

numbers =[
    "",         								              #0
    "1",        								              #1
    "2",        								              #2
    "12",       								              #3
    "3",        								              #4
    "13",       							            	  #5
    "23",       							            	  #6
    "123",      							            	  #7
    "4",        								              #8
    "14",       								              #9
    "24",       								              #10
    "124",      								              #11
    "34",       								              #12
    "134",      								              #13
    "234",      								              #14
    "1234",     								              #15
]

bits = {'1': 13, '2': 19, '3': 21, '4': 23}		#The numbers 13, 19, 21, and 23 correspond to the Raspberry Pi GPIO pin numbers. 1 = LSB, 4 = MSB. Wire your LED's to the aforementioned GPIO pins.

def init():    									              #Initialise pins as outputs.
    for s in bits:
        GPIO.setup(bits[s], GPIO.OUT)
    reset()

def reset():
    for s in bits:
        GPIO.output(bits[s], False)

def count(delay):								              #Binary count function. The 'delay' argument specifies the refresh rate in seconds.
    for n in range (0, 16):
        bits_to_turn_on = numbers[n]
        time.sleep(delay)
        reset()
        for s in bits_to_turn_on:
            GPIO.output(bits[s], True)
            
#Example usage: (Uncomment all to test)
			
#init()

#count(0.5)

#time.sleep(5)

#GPIO.cleanup()
