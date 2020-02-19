from catalog.tasks import scan_catalog, update_catalog
from chibi_gob_mx import catalog



import datetime
import unittest
from unittest.mock import patch, Mock

from catalog.factories import (
    Catalog as Catalog_factory,
    Catalog_with_id as Catalog_with_id_factory
)
from catalog.models import Catalog_pulse, Catalog


class Test_scan_catalog( unittest.TestCase ):
    @patch( 'catalog.models.Catalog.get' )
    def test_should_work( self, catalog_get ):
        catalog_response = catalog.get()
        catalog_total = len( list ( catalog_response.native ) )
        catalog_to_update = Mock()
        catalog_get.return_value = catalog_to_update
        scan_catalog.delay()

        self.assertEqual(
            catalog_total,
            len( catalog_to_update.update_count.call_args_list ) )
        self.assertEqual( catalog_total, len( catalog_get.call_args_list ) )


class test_update_catalog( unittest.TestCase ):
    def test_should_work( self ):
        catalog = Catalog.search()[:1].execute()[0]
        catalog_id = catalog.meta.id
        new_data = { 'count': catalog.count + 10 }
        when = datetime.datetime.utcnow() - datetime.timedelta( days=1 )
        update_catalog( catalog_id, new_data, when )
        result = Catalog._index.flush()
        catalog_v2 = Catalog.get( catalog_id )

        self.assertEqual( catalog_v2.count, new_data[ 'count' ] )
