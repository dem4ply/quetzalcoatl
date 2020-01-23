from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from test_runners import unauthorized as unauthorized

from chibi_user.tests import get_user_test
from catalog.factories import Catalog as Catalog_factory
from test_runners.snippet.response import assert_status_code


class Test_catalog( APITestCase ):
    url_name = 'catalogs:catalog-list'

    def setUp( self ):
        super().setUp()

    def test_should_be_a_list( self ):
        url = reverse( self.url_name )
        response = self.client.get( url )
        assert_status_code( response, status.HTTP_200_OK )
        self.assertIsInstance( response.data, list )
