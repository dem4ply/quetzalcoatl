from unittest import skip
import factory
from chibi_user.tests import get_user_test, get_superuser_test
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from test_runners.snippet.response import (
    assert_status_code, assert_has_pages, get_location
)

from catalog.factories import (
    Catalog_from_cdmx_api as Catalog_from_cdmx_api_factory
)
from catalog.models import Catalog as Catalog


class Test_catalog_create_need_to_be_admin( APITestCase ):
    url_name = 'catalogs:catalog-list'

    def setUp( self ):
        super().setUp()

    def test_should_return( self ):
        url = reverse( self.url_name )
        data = factory.build(
            dict, FACTORY_CLASS=Catalog_from_cdmx_api_factory )
        response = self.client.post( url, data=data )
        assert_status_code( response, status.HTTP_401_UNAUTHORIZED )


class Test_catalog_list( APITestCase ):
    url_name = 'catalogs:catalog-list'

    def setUp( self ):
        super().setUp()

    def test_should_be_a_list( self ):
        url = reverse( self.url_name )
        response = self.client.get( url )
        assert_status_code( response, status.HTTP_200_OK )
        self.assertIsInstance( response.data, list )
        self.assertTrue( response.data )
        assert_has_pages( response )
        for data in response.data:
            self.assertIn( 'pk', data )
            self.assertIn( 'fields', data )
            self.assertIsInstance( data[ 'fields' ], list )


class Test_catalog_create( APITestCase ):
    url_name = 'catalogs:catalog-list'

    def setUp( self ):
        self.client = APIClient( enforce_csrf_checks=True )
        self.super_user, self.super_token  = get_superuser_test()
        self.user, self.user_token = get_user_test()
        self.client.credentials( HTTP_AUTHORIZATION=str( self.super_token ) )

    def test_should_create_the_new_element( self ):
        url = reverse( self.url_name )
        data = factory.build(
            dict, FACTORY_CLASS=Catalog_from_cdmx_api_factory )
        response = self.client.post( url, data=data )
        assert_status_code( response, status.HTTP_201_CREATED )
        response = get_location( response )
        self.assertIsInstance( response.data, dict )
        self.assertTrue( response.data )
        self.assertIn( 'pk', response.data )
        self.assertIn( 'endpoint', response.data )
        self.assertIn( 'origin_url', response.data )
        self.assertIn( 'fields', response.data )
        self.assertTrue( response.data[ 'fields' ] )


class Test_catalog_retrieve( APITestCase ):
    url_name = 'catalogs:catalog-detail'

    def setUp( self ):
        super().setUp()

    def test_should_be_a_dict( self ):
        catalog = Catalog.search()[:1].execute()[0]

        url = reverse( self.url_name, kwargs={ 'pk': catalog.meta.id } )
        response = self.client.get( url )
        assert_status_code( response, status.HTTP_200_OK )
        self.assertIsInstance( response.data, dict )
        self.assertTrue( response.data )
        self.assertIn( 'pk', response.data )
        self.assertIn( 'fields', response.data )
        self.assertIsInstance( response.data[ 'fields' ], list )
        self.assertTrue( response.data[ 'fields' ] )


    def test_should_return_404( self ):
        catalog = Catalog.search()[:1].execute()[0]

        url = reverse( self.url_name, kwargs={ 'pk': '1' } )
        response = self.client.get( url )
        assert_status_code( response, status.HTTP_404_NOT_FOUND )
