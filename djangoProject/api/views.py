from django.shortcuts import render
from rest_framework import generics
from .models import TestModel2, CurrentLocalDevices
from .serializers import TestModel2Serializer, CurrentLocalDevicesSerializer


class TestFieldViewList(generics.ListCreateAPIView):
    queryset = TestModel2.objects.all()
    serializer_class = TestModel2Serializer
    name = 'test-field-list'


class TestFieldViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestModel2.objects.all()
    serializer_class = TestModel2Serializer
    name = 'test-field-details'


class CurrentLocalDevicesViewList(generics.ListCreateAPIView):
    queryset = CurrentLocalDevices.objects.all()
    serializer_class = CurrentLocalDevicesSerializer
    name = "current-local-devices-list"


class CurrentLocalDevicesViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CurrentLocalDevices.objects.all()
    serializer_class = CurrentLocalDevicesSerializer
    name = "current-local-devices-details"
