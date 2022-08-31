from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from hotels_app.models import Hotel, Room, RoomImage
from hotels_app.serializers import HotelSerializer, RoomSerializer, RoomImageSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name', 'stars', 'location']


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend]


class RoomImageViewSe(viewsets.ModelViewSet):
    queryset = RoomImage.objects.all()
    serializer_class = RoomSerializer

