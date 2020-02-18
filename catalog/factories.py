import factory
from faker import Factory as Faker_factory

from .models import Catalog as Catalog_model


fake = Faker_factory.create()


class Catalog( factory.Factory ):
    name = factory.lazy_attribute( lambda x: fake.company() )
    count = factory.lazy_attribute( lambda x: fake.pyint(min_value=0 ) )
    endpoint = factory.lazy_attribute( lambda x: fake.slug() )
    url = factory.lazy_attribute(
        lambda self: 'https://api.datos.gob.mx/v2/' + self.endpoint )
    fields = factory.lazy_attribute( lambda x: fake.pylist( 10, True, 'str' ) )

    class Meta:
        model = Catalog_model


class Catalog_from_origin( factory.Factory ):
    name = factory.lazy_attribute( lambda x: fake.company() )
    count = factory.lazy_attribute( lambda x: fake.pyint(min_value=0 ) )
    endpoint = factory.lazy_attribute( lambda x: fake.slug() )
    url = factory.lazy_attribute(
        lambda self: 'https://api.datos.gob.mx/v2/' + self.endpoint )
    variables = factory.lazy_attribute( lambda x: fake.pylist( 10, True, 'str' ) )

    class Meta:
        model = Catalog_model


class Catalog_with_id( factory.Factory ):
    id = factory.lazy_attribute( lambda x: fake.md5( raw_output=False ) )
    name = factory.lazy_attribute( lambda x: fake.company() )
    count = factory.lazy_attribute( lambda x: fake.pyint(min_value=0 ) )
    endpoint = factory.lazy_attribute( lambda x: fake.slug() )
    url = factory.lazy_attribute(
        lambda self: 'https://api.datos.gob.mx/v2/' + self.endpoint )
    fields = factory.lazy_attribute( lambda x: fake.pylist( 10, True, 'str' ) )

    class Meta:
        model = Catalog_model


class Catalog_from_cdmx_api( factory.Factory ):
    id = factory.lazy_attribute( lambda x: fake.md5( raw_output=False ) )
    name = factory.lazy_attribute( lambda x: fake.company() )
    count = factory.lazy_attribute( lambda x: fake.pyint(min_value=0 ) )
    endpoint = factory.lazy_attribute( lambda x: fake.slug() )
    origin_url = factory.lazy_attribute(
        lambda self: 'https://api.datos.gob.mx/v2/' + self.endpoint )
    fields = factory.lazy_attribute(
        lambda x: fake.pylist( 10, True, 'str' ) )

    class Meta:
        model = Catalog_model
