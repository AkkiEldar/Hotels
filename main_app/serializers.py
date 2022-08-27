from rest_framework import serializers
from main_app.models import Info, OurPartners, AboutUs, RecomendationHotels


class RecomendationHotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecomendationHotels
        fields = '__all__'


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'


class OurPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurPartners
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'
