from rest_framework import serializers
from .models import Driver


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ['full_name', 'user']
