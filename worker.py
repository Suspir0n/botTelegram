from celery import Celery

# Celery configuration
CELERY_BROKER_URL = 'amqp://rabbitmq:rabbitmq@rabbit:5672/'
CELERY_RESULT_BACKEND = 'rpc://'


# Initialize celery_task
_celery = Celery('worker', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@_celery.task()
def post_user(receive_json):
    pass

@_celery.task()
def get_user():
    pass