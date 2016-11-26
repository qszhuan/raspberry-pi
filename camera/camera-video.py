from picamera import PiCamera
from time import sleep
import os
from datetime import datetime

folder = '/home/pi/Pictures/'
create_folder = 'mkdir {0} -p'.format(folder)
os.system(create_folder)

camera = PiCamera()
camera.rotation = 180
#camera.start_preview()
sleep(5)

print('started...')

while True:
  
  print('taking picture ...', datetime.now())
  camera.start_recording('{0}/{1:%Y-%m-%d_%H.%M.%S}.h264'.format(folder, datetime.now()))
  sleep(60)
  camera.stop_recording()
  print('done, then sleep 1h')
  sleep(60*60)

#camera.stop_preview()
