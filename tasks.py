from celery import Celery
import os
import shutil
import random
from celery.exceptions import SoftTimeLimitExceeded
import subprocess

app = Celery('tasks')
app.config_from_object('celeryconfig')


@app.task
def add(x, y):
    return x + y


@app.task(bind=True)
def play(self):
    prc = None
    try:
        files = os.listdir('./rings')
        commands = ['afplay', 'omxplayer']
        available_players = [each for each in commands if shutil.which(each) is not None]
        if any(available_players):
            song = random.choice(files)
            prc = subprocess.Popen(available_players[0] + ' ./rings/' + song, shell=True)
            prc.wait()
            return 'Played song ' + song
        else:
            return 'Could not find the player.'
    except SoftTimeLimitExceeded:
        prc.terminate()
        return 'Exceeded soft time limit.'


play.delay()

