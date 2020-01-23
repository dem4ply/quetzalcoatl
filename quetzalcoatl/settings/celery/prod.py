import os

# from kombu import Exchange, Queue
# from celery.schedules import crontab
# from datetime import timedelta


url_key = os.environ[ 'QUETZALCOATL__RABBITMQ__KEY__URL' ]
celery_url = os.environ[ url_key ]


BROKER_URL = celery_url
RESULT_BACKEND = celery_url
CELERY_RESULT_BACKEND = celery_url

'''
task_annotations = {
    '*': {
        'rate_limit': '5/s'
    }
}
'''

# beat_schedule = 'djcelery.schedulers.DatabaseScheduler'

# TASK_QUEUES = (
#     Queue( 'default', Exchange( 'task', 'topic' ), routing_key='default' ),
#     Queue(
#         'debug', Exchange( 'task_debug', 'topic' ), routing_key='*.debug.*' ),
# )
#
# TASK_DEFAULT_QUEUE = 'default'
# TASK_DEFAULT_EXCHANGE = "tasks"
# TASK_DEFAULT_EXCHANGE_TYPE = "topic"
# TASK_DEFAULT_ROUTING_KEY = "task.default"
#
# TASK_ROUTES = {
#     'default': {
#         'binding_key': 'task.#',
#     },
#     'reader_moe.tasks.debug_task': {
#         'queue': 'debug',
#         'binding_key': 'task.debug.*',
#         'exchange': 'task_debug'
#     }
# }
#
# beat_schedule = { }

RESULT_SERIALIZER = 'json'
TASK_SERIALIZER = 'json'

CELERY_ALWAYS_EAGER = False
