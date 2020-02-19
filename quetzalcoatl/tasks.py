from celery.utils.log import get_task_logger

from .task_class import Task_base
from quetzalcoatl.app_celery import quetzalcoatl_task as celery_task


logger = get_task_logger( 'celery.task.quetzalcoatl' )


@celery_task.task( bind=True, base=Task_base, ignore_result=True )
def debug_task( self, *args, **kw ):
    logger.debug(
        "execute task for debug",
        extra={ 'params': { 'args': args, 'kargs': kw } } )
