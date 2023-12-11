from rest_framework import serializers
from . import models


class DrizzleSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Drizzle
        fields = ('temperature', 'city')

