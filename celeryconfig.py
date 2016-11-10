broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
# timezone = 'Europe/Oslo'
# enable_utc = True
task_track_started = True
task_soft_time_limit = 5

task_routes = {
    # 'tasks.add': 'default',
    # 'tasks.play': 'media',
}

task_annotations = {
    'tasks.add': {'rate_limit': '10/m'},
    # 'tasks.play': {'rate_limit': '1/m'},
}


#
