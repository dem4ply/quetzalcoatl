from rest_framework.response import Response
from chibi_django import view_set
from chibi_django.pagination import Paginate_search_es
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import decorators

from .models import Catalog as Catalog_model
from .serializers import (
    Catalog_create as Catalog_create_serializer,
    Catalog_list as Catalog_list_serializer,
)


class Catalog( view_set.Elastic_model_viewset ):
    permission_classes = [ AllowAny ]
    queryset = Catalog_model.search()
    serializer_class = {
        'list': Catalog_list_serializer,
        'retrieve': Catalog_list_serializer,
        'create': Catalog_create_serializer,

    }
    pagination_class = Paginate_search_es

    @decorators.permission_classes( [ IsAdminUser ] )
    def create( self, request, *args, **kw ):
        return super().create( request, *args, **kw )
