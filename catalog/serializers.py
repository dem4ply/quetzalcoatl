from .models import Catalog as Catalog_model
from rest_framework import serializers


class Catalog_list( serializers.ListSerializer ):
    pass



class Catalog( serializers.Serializer ):
    count = serializers.IntegerField()
    endpoint = serializers.CharField()
    url = serializers.CharField()
    fields = serializers.ListField(
        serializers.CharField(), source='variables' )

    def create( self, data, **kw ):
        import pdb
        pdb.set_trace()
        pass

    class Meta:
        model = Catalog_model
