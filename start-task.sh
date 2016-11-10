# start tasks
celery -A tasks worker --loglevel=info &

# monitoring
celery -A tasks flower &
