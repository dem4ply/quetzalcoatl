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
        document_save.assert_called()

    @patch( 'elasticsearch_dsl.Document.save' )
    def test_should_add_the_update_at_when_do_the_save( self, document_save ):
        catalog = Catalog_factory.build()
        self.assertIsNone( catalog.update_at )
        catalog.save()
        self.assertIsInstance( catalog.update_at, datetime.datetime )
        document_save.assert_called()

    @patch( 'elasticsearch_dsl.Document.save' )
    def test_should_update_the_update_at_when_do_the_save( self, document_save ):
        catalog = Catalog_factory.build()
        catalog.save()
        update_at = catalog.update_at
        catalog.save()
        self.assertLess( update_at, catalog.update_at )
        document_save.assert_called()


class Test_catalog_update_count( unittest.TestCase ):
    @patch( 'elasticsearch_dsl.Document.save' )
    def setUp( self, save ):
        super().setUp()
        self.catalog = Catalog_with_id_factory.build()
        self.catalog.save()

    @patch( 'catalog.models.Catalog.save' )
    @patch( 'catalog.models.Catalog_pulse.save' )
    def test_when_update_count_should_save_the_pulse(
            self, catalog_save, catalog_pulse_save ):
        count = self.catalog.count + 10
        self.catalog.update_count( count )
        catalog_save.assert_called()
        catalog_pulse_save.assert_called()

    @patch( 'elasticsearch_dsl.Document.save' )
    def test_should_create_the_pulse(
            self, document_save ):
        count = self.catalog.count + 10
        pulse = self.catalog.update_count( count )

    @patch( 'elasticsearch_dsl.Document.save' )
    def test_relative_count_should_be_correct(
            self, document_save, ):
        count = self.catalog.count + 10
        pulse = self.catalog.update_count( count )
        self.assertEqual( pulse.relative_count, 10 )


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


class Test_catalog_pulse( unittest.TestCase ):
    @patch( 'elasticsearch_dsl.Document.save' )
    def test_on_save_should_set_the_create_at( self, document_save ):
        pulse = Catalog_pulse()
        pulse.save()
        document_save.assert_called()
        self.assertIsNotNone( pulse.create_at )
        self.assertIsInstance( pulse.create_at, datetime.datetime )


    @patch( 'elasticsearch_dsl.Document.save' )
    def test_when_have_the_create_at_should_no_changed( self, document_save ):
        date = datetime.datetime( 2000, 1, 1 )
        pulse = Catalog_pulse( create_at=date )
        pulse.save()
        self.assertEqual( pulse.create_at, date )
