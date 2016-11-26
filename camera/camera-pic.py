from picamera import PiCamera
from time import sleep
import os
from datetime import datetime

folder = '/home/pi/Pictures/pic_{:%Y-%m-%d_%H.%M.%S}'.format(datetime.now())
create_folder = 'mkdir {0} -p'.format(folder)
os.system(create_folder)

camera = PiCamera()
#camera.rotation = 180
camera.start_preview()
sleep(5)
for i in range(5):
  camera.capture('{0}/{1}.jpg'.format(folder, i))
  sleep(1)
camera.stop_preview()
