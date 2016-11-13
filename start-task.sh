#!/usr/bin/env bash

# virtual env
workon rpi

# start tasks
celery -A tasks worker --loglevel=info -B &

# monitoring
#celery -A tasks flower &
