from chibi_django import view_set
from chibi_django.pagination import Paginate_search_es
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Catalog as Catalog_model
from .serializers import Catalog as Catalog_serializer


class Catalog( view_set.Multi_serializer_viewset ):
    permission_classes = [ AllowAny ]
    queryset = Catalog_model.search()
    serializer_class = Catalog_serializer
    pagination_class = Paginate_search_es

    def list( self, request, *args, **kw ):
        queryset = self.filter_queryset( self.get_queryset() )

        page = self.pagination_class()
        return page.get_paginated_response(
            queryset, request, serializer=self.serializer_class )

    def retrieve( self, request, *args, **kw ):
        instance = self.get_object()
        serializer = self.get_serializer( instance,
                                          serializer_name='retrieve' )
        return Response( serializer.data )

    def create( self, request, *args, **kw ):
        serializer = self.get_serializer(
            data=self.create_build_data( request.data ),
            serializer_name='create' )
        serializer.is_valid( raise_exception=True )
        self.perform_create( serializer )
        headers = self.get_success_headers( serializer.data )
        return Response( status=status.HTTP_201_CREATED, headers=headers )

    def perform_create( self, serializer ):
        serializer.save()
