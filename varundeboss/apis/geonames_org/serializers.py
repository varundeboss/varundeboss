from .models import Geoname

from rest_framework import serializers

class GeonameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Geoname
        fields = ('url', 'name',)