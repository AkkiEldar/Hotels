from django.contrib.auth.models import User
from django.db import models


class Hotel(models.Model):
    STARS_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    hotel_id = models.AutoField(primary_key=True)
    logo = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    location = models.URLField()
    description = models.TextField()
    whatsapp = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    contact = models.CharField(max_length=1000)
    rooms_count = models.IntegerField()
    # rooms = models.ForeignKey(Room, on_delete=models.CASCADE)
    star = models.CharField(
        max_length=2,
        choices=STARS_CHOICES
    )

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return f'{self.name}'


class Room(models.Model):
    floor = models.PositiveIntegerField(default=1)
    room_number = models.IntegerField()
    is_active = models.BooleanField(default=True)
    room_type = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField(default=1)
    description = models.TextField()
    how_mach_people = models.PositiveIntegerField(default=1)
    hotel = models.ForeignKey(Hotel, to_fields='hotel_id', on_delete=models.CASCADE)
    # room_image = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None, default='0.jpeg')


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)


# class Booking(models.Model):
#
#     check_in = models.DateField(auto_now=False)
#     check_out = models.DateField()
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     guest = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     booking_id = models.CharField(max_length=100, default="null")
#
#     def __str__(self):
#         return self.guest.username
