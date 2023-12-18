from rest_framework import serializers
from . import models


class DrizzleSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.LeaderDrizzle
        fields = ('__all__',)

