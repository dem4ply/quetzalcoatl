from catalog.models import Catalog
from django.db import migrations, models
from chibi_gob_mx import catalog
from catalog.serializers import Catalog as Catalog_serializer


def create_catalog_index( apps, schema_editor ):
    if not Catalog._index.exists():
        result = Catalog.init()
    if Catalog.search().count() < 1:
        response = catalog.get()
        import pdb
        pdb.set_trace()
        serializer = Catalog_serializer( data=response.native, many=True )
        serializer.is_valid( raise_exception=True )
        serializer.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunPython( create_catalog_index ),
    ]
