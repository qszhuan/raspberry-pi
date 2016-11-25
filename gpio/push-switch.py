import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # P0 

on = False

while True:
    # print('waiting')
    #input_state = GPIO.wait_for_edge(17, GPIO.RISING)
    #print('got state', input_state)
    input_state = GPIO.input(17)
    if input_state == False:
        print('Button Pressed')
	GPIO.output(18, GPIO.HIGH if not on else GPIO.LOW)
	on = not on
        time.sleep(0.5)
