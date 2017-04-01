from .models import Thing

from rest_framework import serializers

class SchemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thing
        fields = "__all__"