from django.db import models


class RecomendationHotels(models.Model):
    # hotels = models.ForeignKey(hotels_app) # ('location','stars','price')# по дефолту
    logo = models.ImageField()
    contacts = models.CharField(max_length=255)
    image = models.ImageField()
    whatsapp = models.URLField()
    telegram = models.URLField()
    instagram = models.URLField()


class Info(models.Model):
    # language =
    our_contacts = models.CharField(max_length=255)
    logo = models.ImageField()
    email = models.EmailField()
    whatsapp = models.URLField()
    telegram = models.URLField()
    instagram = models.URLField()


class OurPartners(models.Model):
    partner = models.CharField(max_length=255)
    urls_partner = models.URLField()
    logo = models.ImageField()


class AboutUs(models.Model):
    text = models.TextField()
    other_service = models.TextField()
    image = models.ImageField()

