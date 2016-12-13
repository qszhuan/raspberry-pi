import RPi.GPIO as GPIO
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
IN_PIN = 18
LED_PIN = 17

GPIO.setup(IN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.output(LED_PIN, GPIO.LOW)

def turn_on(led_pin):
  GPIO.output(led_pin, GPIO.HIGH)

def turn_off(led_pin):
  GPIO.output(led_pin, GPIO.LOW)

count = 0
while True:
  i=GPIO.input(IN_PIN)                        
  if(count == 1000):
    turn_off(LED_PIN)
  count += 1
  if i==1:                                
    print(datetime.datetime.now(), "Vibration detected",i)
    time.sleep(0.1)
    count = 0
    turn_on(LED_PIN)
