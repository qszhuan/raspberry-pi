from celery.schedules import crontab
from celery.schedules import solar
import datetime

lat_lon = {
    'melbourne': [-37.8097515, 145.2331785]
}

broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']

task_track_started = True
task_soft_time_limit = 60 * 5

timezone = 'Australia/Melbourne'
task_routes = {
    # 'tasks.add': 'default',
    # 'tasks.play': 'media',
}

# music_folder = '/Users/TWIS/Music/网易云音乐'
music_folder = '/home/pi/Music'

beat_schedule = {
    # 'test-schedule': {
    #     'task': 'tasks.test',
    #     'schedule': 10,
    #     'args': ('test message',)
    # },

    'timer-every-hour-between-8-21': {
        'task': 'tasks.timer',
        'schedule': crontab(hour='8-21', minute=0),
        'args': ('clock',)
    },

    'alarm-every-workday-morning': {
        'task': 'tasks.play',
        'schedule': crontab(minute='1,8', hour='8', day_of_week='1,2,3,4,5,6,0'),
        'args': (music_folder,),
    },

    'record-at-melbourne-dawn_astronomical': {
        'task': 'tasks.solar',
        'schedule': solar('dawn_astronomical', *lat_lon['melbourne']),
        'args': ('dawn_astronomical',),
    },
    'record-at-melbourne-dawn_nautical': {
        'task': 'tasks.solar',
        'schedule': solar('dawn_nautical', *lat_lon['melbourne']),
        'args': ('dawn_nautical',),
    },
    'record-at-melbourne-dawn_civil': {
        'task': 'tasks.solar',
        'schedule': solar('dawn_civil', *lat_lon['melbourne']),
        'args': ('dawn_civil',),
    },
    'record-at-melbourne-sunset': {
        'task': 'tasks.solar',
        'schedule': solar('sunset', *lat_lon['melbourne']),
        'args': ('sunset',),
    },
    'record-at-melbourne-sunrise': {
        'task': 'tasks.solar',
        'schedule': solar('sunrise', *lat_lon['melbourne']),
        'args': ('sunrise',),
    },
    # 'record-at-melbourne-solar_noon': {
    #     'task': 'tasks.solar',
    #     'schedule': solar('solar_noon', *lat_lon['melbourne']),
    #     'args': ('solar_noon',),
    # },
    'record-at-melbourne-dusk_civil': {
        'task': 'tasks.solar',
        'schedule': solar('dusk_civil', *lat_lon['melbourne']),
        'args': ('dusk_civil',),
    },
    'record-at-melbourne-dusk_nautical': {
        'task': 'tasks.solar',
        'schedule': solar('dusk_nautical', *lat_lon['melbourne']),
        'args': ('dusk_nautical',),
    },
    'record-at-melbourne-dusk_astronomical': {
        'task': 'tasks.solar',
        'schedule': solar('dusk_astronomical', *lat_lon['melbourne']),
        'args': ('dusk_astronomical',),
    },
}

task_annotations = {
    'tasks.add': {'rate_limit': '10/m'},
    # 'tasks.play': {'rate_limit': '1/m'},
}


#
