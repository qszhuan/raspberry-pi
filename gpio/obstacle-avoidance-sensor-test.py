import RPi.GPIO as GPIO
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
IN_PIN = 18
GPIO.setup(IN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

while True:
          i=GPIO.input(IN_PIN)                        
          if i==0:                                
               print(datetime.datetime.now(), "Obstacle detected",i)
               time.sleep(0.1)
