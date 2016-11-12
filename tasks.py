from celery import Celery
import os
import shutil
import random
from celery.exceptions import SoftTimeLimitExceeded
import subprocess
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
    solar_event = '{0:%A, %d. %B %Y %I:%M%p} : Event: {1}'.format(now, event)
    print(solar_event)
    return solar_event


@app.task(bind=True)
def timer(self, timer_type, ):
    if timer_type == 'clock':
        message = 'Today is {0:%A}, the time now is {0:%I:%M%p}'.format(datetime.datetime.now())
        say(message)
        return message

@app.task(bind=True)
def play(self, dir_name='./rings'):
    prc = None
    try:
        files = os.listdir(dir_name)
        commands = ['afplay', 'omxplayer']
        available_players = [each for each in commands if shutil.which(each) is not None]
        if any(available_players):
            song = random.choice(files)
            command = '{0} "{1}/{2}"'.format(available_players[0], dir_name, song)
            print(command)
            prc = subprocess.Popen(command, shell=True)
            prc.wait()
            return '[{0}]: Played song{1}'.format(datetime.datetime.now(), song)
        else:
            return 'Could not find the player.'
    except SoftTimeLimitExceeded:
        #prc.terminate()
        os.system("kill -9 {0}".format(prc.pid))
        return 'Exceeded soft time limit.'


def say(message):
    platform = os.sys.platform
    if platform == 'darwin':
        os.system('say "{0}"'.format(message))
    elif platform == 'linux':
        os.system('echo "{0}" | festival --tts'.format(message))
