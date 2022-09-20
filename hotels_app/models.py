from django.contrib.auth.models import User

from django.db import models
from authentication_app.models import Account


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
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    # room_image = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None, default='0.jpeg')


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)


# class BookingDetails(models.Model):
#     BOOKING_STATUS = (('A', 'Availed'),
#                       ('B', 'Booked'),
#                       ('C1', 'Cancelled by user'),
#                       ('C2', 'Cancelled by hotel')
#                       )
#     booking_id = models.AutoField(primary_key=True)
#     guest = models.ForeignKey(Account, to_field='user_name')
#     hotel = models.ForeignKey(Account, to_field='hotel_id')
#     booking_status = models.CharField(max_length=2, choices=BOOKING_STATUS)
#     check_in_date = models.CharField(max_length=15)
#     check_out_date = models.CharField(max_length=15)
#     check_in_time = models.CharField(max_length=15)
#     check_out_time = models.CharField(max_length=15)
#     room = models.ForeignKey(Room, to_field='room_type')
#     total_guests = models.PositiveIntegerField(default=0)
#     total_days = models.PositiveIntegerField(default=0)
#     total_cost = models.DecimalField(max_digits=15, decimal_places=2)
#     discounted_price = models.DecimalField(max_digits=15, decimal_places=2)
#     total_rooms = models.PositiveIntegerField(default=0)
#     booking_date = models.CharField(max_length=15)
