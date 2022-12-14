#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_PIR = 7

GPIO.setup(GPIO_PIR, GPIO.IN)

try: 
	while True: 

		currentstate = GPIO.input(GPIO_PIR)
		print (currentstate)

except KyeboardInterrupt:
	print("End")

	
