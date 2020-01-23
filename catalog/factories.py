import factory
from faker import Factory as Faker_factory

from .models import Catalog as Catalog_model


faker = Faker_factory.create()


class Catalog( factory.Factory ):
    name = factory.lazy_attribute( lambda x: faker.company() )
    count = factory.lazy_attribute( lambda x: faker.fake.pyint(min_value=0 ) )
    endpoint = factory.lazy_attribute( lambda x: fake.slug )
    url = factory.lazy_attribute(
        lambda x: 'https://api.datos.gob.mx/v2/' + self.endpoint )
    fields = factory.lazy_attribute(
        lambda x: fake.pylist(
            str, nb_elements=10, variable_nb_elements=True ) )

    class Meta:
        model = Catalog_model
