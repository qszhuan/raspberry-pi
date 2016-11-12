from celery import Celery
import os
import shutil
import random
from celery.exceptions import SoftTimeLimitExceeded
import subprocess
from celery.schedules import crontab
import datetime

app = Celery('tasks')
app.config_from_object('celeryconfig')

#
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
#
#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)
#
#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         test.s('Happy Mondays!'),
#     )


@app.task
def solar(event):
    now = datetime.datetime.now()
    solar_event = '{0} : Event: {1}'.format(now, event)
    print(solar_event)
    return solar_event


@app.task
def add(a, b):
    print('Result is ', a + b)
    return a + b


@app.task(bind=True)
def play(self, song_name=""):
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
