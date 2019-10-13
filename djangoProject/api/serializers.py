from rest_framework import serializers
from .models import TestModel2, CurrentLocalDevices

# Create your views here.


class TestModel2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestModel2
        fields = ['test_field', 'x']


class CurrentLocalDevicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CurrentLocalDevices
        fields = ['mac_number']
