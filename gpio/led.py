import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

i = 0
while i < 10:
  print "LED on"
  time.sleep(1)
  GPIO.output(18,GPIO.HIGH)
  time.sleep(1)

  print "LED off"
  GPIO.output(18,GPIO.LOW)

  i +=1
