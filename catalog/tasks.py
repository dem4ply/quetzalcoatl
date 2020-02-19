import datetime
from celery.utils.log import get_task_logger

from quetzalcoatl.app_celery import quetzalcoatl_task as celery_task
from quetzalcoatl.task_class import Task_base
from chibi_gob_mx import catalog
from celery import group
from catalog.models import Catalog
from elasticsearch.exceptions import NotFoundError
from catalog.serializers import Catalog_create


logger = get_task_logger( 'celery.task.catalog' )


@celery_task.task(
    bind=True, base=Task_base, ignore_results=True, max_retries=3 )
def scan_catalog( self, *args, **kw ):
    response = catalog.get()
    when = datetime.datetime.utcnow()
    g = group( update_catalog.s( n.id, n, when ) for n in response.native )
    g.delay()


@celery_task.task(
    bind=True, base=Task_base, ignore_results=True, max_retries=3 )
def update_catalog( self, catalog_id, new_data, when ):
    try:
        catalog = Catalog.get( catalog_id )
    except NotFoundError:
        serializer = Catalog_create( data=new_data )
        serializer.is_valid( raise_exception=True )
        serializer.save()
        return

    if 'count' not in new_data:
        raise ValueError( "los nuevos datos no tienen count" )
    catalog.update_count( new_data[ 'count' ] )
