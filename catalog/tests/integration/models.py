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




class test_update_catalog( unittest.TestCase ):
    def test_should_work( self ):
        catalog = Catalog.search()[:1]
        catalog = catalog.execute()[0]
        catalog_id = catalog.meta.id
        new_data = { 'count': catalog.count + 10 }
        when = datetime.datetime.utcnow() - datetime.timedelta( days=1 )
        update_catalog( catalog_id, new_data, when )
        result = Catalog._index.flush()
        catalog_v2 = Catalog.get( catalog_id )

        self.assertEqual( catalog_v2.count, new_data[ 'count' ] )
