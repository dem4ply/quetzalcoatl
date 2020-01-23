from django.db import models
from django.utils.translation import ugettext_lazy as _
from chibi_django.models import Chibi_model
from elasticsearch_dsl import Document, MetaField, field


class Catalog( Document ):
    create_at = field.Date()
    update_at = field.Date()
    count = field.Integer()
    endpoint = field.Text()
    url = field.Keyword()
    fields = field.Text( multi=True )

    class Index:
        name = 'quetzalcoatl__catalog'
        settings = { 'number_of_shards': 2, 'number_of_replicas': 1 }

    class Meta:
        numeric_detection = MetaField( False )
        date_detection = MetaField( False )


__all__ = [ 'Catalog' ]
