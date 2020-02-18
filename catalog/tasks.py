from celery.utils.log import get_task_logger

from quetzalcoatl.app_celery import quetzalcoatl_task as celery_task
from quetzalcoatl.task_class import Task_base
from profiles.models import Profile, COMPLETE, FAIL, ERROR, PROCCESS, WAIT


logger = get_task_logger( 'celery.task.package' )


@celery_task.task(
    bind=True, base=Task_base, ignore_results=True, max_retries=3 )
def hello( self, *args, **kw ):
    print( args, kw )
