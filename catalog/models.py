import datetime
from chibi_django.snippet.elasticsearch import build_index_name

from elasticsearch_dsl import Document, MetaField, field


__all__ = [ 'Catalog', 'Catalog_pulse' ]


class Catalog( Document ):
    count = field.Integer()
    create_at = field.Date()
    endpoint = field.Text()
    fields = field.Text( multi=True )
    update_at = field.Date()
    origin_url = field.Keyword()

    class Index:
        name = build_index_name( 'catalog' )
        settings = { 'number_of_shards': 2, 'number_of_replicas': 1 }

    class Meta:
        numeric_detection = MetaField( False )
        date_detection = MetaField( False )

    def save( self, *args, **kw ):
        if not getattr( self.meta, 'id', False ):
            if getattr( self, 'id', False ):
                self.meta.id = self.id
                del self.id
            self.create_at = datetime.datetime.utcnow()
        self.update_at = datetime.datetime.utcnow()
        return super().save( *args, **kw )

    def build_pulse( self, new_count=None ):
        relative_count = 0
        if new_count is not None:
            relative_count = new_count - self.count
        pulse = Catalog_pulse(
            catalog_id=self.meta.id, count=new_count,
            relative_count=relative_count )
        return pulse


class Catalog_pulse( Document ):
    catalog_id = field.Keyword()
    count = field.Integer()
    create_at = field.Date()
    relative_count = field.Integer()
    update_at = field.Date()

    class Index:
        name = build_index_name( 'catalog_pulse' )
        settings = { 'number_of_shards': 2, 'number_of_replicas': 1 }

    class Meta:
        numeric_detection = MetaField( False )
        date_detection = MetaField( False )

    def save( self, *args, **kw ):
        if not getattr( self.meta, 'id', False ):
            self.create_at = datetime.datetime.utcnow()
        self.update_at = datetime.datetime.utcnow()
        return super().save( *args, **kw )
