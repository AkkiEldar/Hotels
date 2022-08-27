from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from main_app.models import Info, OurPartners, AboutUs , RecomendationHotels
from main_app.serializers import InfoSerializer, OurPartnersSerializer, AboutUsSerializer, RecomendationHotelsSerializer


class RecomendationHotelsViewSet(viewsets.ModelViewSet):
    queryset = RecomendationHotels.objects.all()
    serializer_class = RecomendationHotelsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class OurPartnersViewSet(viewsets.ModelViewSet):
    queryset = OurPartners.objects.all()
    serializer_class = OurPartnersSerializer


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
