import datetime
import unittest
from unittest.mock import patch

from catalog.factories import (
    Catalog as Catalog_factory,
    Catalog_with_id as Catalog_with_id_factory
)
from catalog.models import Catalog_pulse


class Test_catalog_save_dates( unittest.TestCase ):
    @patch( 'elasticsearch_dsl.Document.save' )
    def test_should_add_the_create_at_when_do_the_save( self, document_save ):
        catalog = Catalog_factory.build()
        self.assertIsNone( catalog.create_at )
        catalog.save()
        self.assertIsInstance( catalog.create_at, datetime.datetime )
        document_save.asseert_called()

    @patch( 'elasticsearch_dsl.Document.save' )
    def test_should_add_the_update_at_when_do_the_save( self, document_save ):
        catalog = Catalog_factory.build()
        self.assertIsNone( catalog.update_at )
        catalog.save()
        self.assertIsInstance( catalog.update_at, datetime.datetime )
        document_save.asseert_called()

    @patch( 'elasticsearch_dsl.Document.save' )
    def test_should_update_the_update_at_when_do_the_save( self, document_save ):
        catalog = Catalog_factory.build()
        catalog.save()
        update_at = catalog.update_at
        catalog.save()
        self.assertLess( update_at, catalog.update_at )
        document_save.asseert_called()


class Test_catalog_build_pulse( unittest.TestCase ):
    @patch( 'elasticsearch_dsl.Document.save' )
    def setUp( self, save ):
        super().setUp()
        self.catalog = Catalog_with_id_factory.build()
        self.catalog.save()

    def test_should_create_a_instance_of_catalog_pulse( self ):
        pulse = self.catalog.build_pulse()
        self.assertIsInstance( pulse, Catalog_pulse )

    def test_default_should_create_a_0_pulse( self ):
        pulse = self.catalog.build_pulse()
        self.assertEqual( pulse.relative_count, 0 )

    def test_should_add_the_relative_pulse_positive( self ):
        pulse = self.catalog.build_pulse( self.catalog.count + 10 )
        self.assertEqual( pulse.relative_count, 10 )

    def test_should_add_the_relative_pulse_negative( self ):
        pulse = self.catalog.build_pulse( self.catalog.count - 10 )
        self.assertEqual( pulse.relative_count, -10 )
