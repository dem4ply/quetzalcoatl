from chibi.snippet.dict import replace_keys
from .models import (
    Catalog as Catalog_model,
    Catalog_pulse as Catalog_pulse_model,
)
from chibi_django.serializers_fields import (
    parametrise_hyperlink_identity_field
)
from rest_marshmallow import Schema, fields as f
from rest_framework import serializers


class Catalog_create( serializers.Serializer ):
    id = serializers.CharField( write_only=True )
    count = serializers.IntegerField()
    endpoint = serializers.CharField()
    origin_url = serializers.URLField()
    fields = serializers.ListField(
        child=serializers.CharField( allow_blank=True ) )
    name = serializers.CharField( required=False )
    url = parametrise_hyperlink_identity_field(
        lookup_obj_fields=( ( 'pk', 'meta.id', ), ),
        view_name='catalog:catalog-detail' )

    class Meta:
        model = Catalog_model

    def get_id( self, data ):
        return data.meta.id

    def create( self, data, **kw ):
        model = self.Meta.model( **data )
        result = model.save()
        pulse = model.build_pulse()
        pulse.save()
        return model


class Catalog_list( serializers.Serializer ):
    pk = serializers.CharField( source='meta.id' )
    count = serializers.IntegerField()
    endpoint = serializers.CharField()
    origin_url = serializers.URLField()
    fields = serializers.ListField( child=serializers.CharField() )
    name = serializers.CharField( required=False )

    url = parametrise_hyperlink_identity_field(
        lookup_obj_fields=( ( 'pk', 'meta.id', ), ),
        view_name='catalog:catalog-detail' )

    class Meta:
        model = Catalog_model
