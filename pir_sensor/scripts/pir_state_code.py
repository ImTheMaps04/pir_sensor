#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO_PIR = 11

GPIO.setup(GPIO_PIR, GPIO.IN)

try: 
	while True: 

		currentstate = GPIO.input(GPIO_PIR)
		print (currentstate)
		
		time.sleep(0.1)
		
except KeyboardInterrupt:
	print("End")

GPIO.cleanup()	
