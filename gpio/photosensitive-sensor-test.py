import RPi.GPIO as GPIO, time, os      

PIN_IN = 17 
PIN_OUT = 18

DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_IN, GPIO.IN)
GPIO.setup(PIN_OUT, GPIO.OUT)

def isBright ():
  return GPIO.input(PIN_IN) == GPIO.LOW

GPIO.output(PIN_OUT, GPIO.LOW)
lightOn = False

while True:
  time.sleep(0.5)
  if isBright():
    if lightOn:
      print("It's day, turn off light")
      GPIO.output(PIN_OUT, GPIO.LOW)
      lightOn = False
  elif not lightOn:
    print("It's night, turn on light")
    GPIO.output(PIN_OUT, GPIO.HIGH) 
    lightOn = True
