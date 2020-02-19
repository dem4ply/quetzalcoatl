from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings


__all__ = [ 'quetzalcoatl_task' ]

os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', 'quetzalcoatl.settings' )

quetzalcoatl_task = Celery( 'quetzalcoatl' )

quetzalcoatl_task.config_from_object( 'django.conf:settings' )
quetzalcoatl_task.autodiscover_tasks( lambda: settings.INSTALLED_APPS )
