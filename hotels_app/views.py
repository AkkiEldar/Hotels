import datetime
from email.message import EmailMessage

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.urls import reverse

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from hotels_app.models import Hotel, Room, RoomImage  # BookingDetails
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
    serializer_class = RoomImageSerializer

#
# def booking(request):
#
#     if 'username' not in request.session:
#         return redirect('home')
#     if request.is_ajax():
#         request_no = request.GET.get('request_no')
#         if int(request_no) == 1:
#             room_type = request.GET.get('room_type')
#             room_price = Room.objects.get(room_type=room_type).price_per_day
#             rooms_available = len(Room.objects.filter(room_id=room_type).filter(room_status='V'))
#             return JsonResponse({'room_price': room_price, 'rooms_available': rooms_available})
#         elif int(request_no) == 2:
#             room_type = request.GET.get('room_type')
#             no_of_days = request.GET.get('no_of_days')
#             for record in records:
#                 low, high = map(int, record.length_of_stay.split(':'))
#                 if str(high).strip() != '-1':
#                     if low < int(no_of_days) <= high:
#                         return JsonResponse({'discount_id': record.discount_id, 'offer_percent': record.offer_percent,
#                                              'message': 'success'})
#                 elif str(high).strip() == '-1':
#                     if int(no_of_days) > low:
#                         return JsonResponse({'discount_id': record.discount_id, 'offer_percent': record.offer_percent,
#                                              'message': 'success'})
#             return JsonResponse({'message': 'none'})
#
#     if request.method == 'POST':
#         new_booking = BookingDetails()
#         new_booking.guest_id = request.session['user_id']
#         new_booking.booking_status = "B"
#         new_booking.check_in_date = request.POST.get('check_in_date')
#         new_booking.check_in_time = request.POST.get('check_in_time')+request.POST.get('session1')
#         new_booking.check_out_date = request.POST.get('check_out_date')
#         new_booking.check_out_time = request.POST.get('check_out_time')+request.POST.get('session2')
#         new_booking.total_guests = request.POST.get('total_guests')
#         new_booking.total_days = request.POST.get('total_days')
#         new_booking.total_rooms = request.POST.get('total_rooms')
#         new_booking.discounted_price = float(request.POST.get('discounted_price'))
#         new_booking.total_cost = float(request.POST.get('total_cost'))
#         new_booking.booking_date = datetime.datetime.today().strftime('%Y-%m-%d')
#         new_booking.discount_id = request.POST.get('discount_id')
#         complete_id = request.POST.get('hotel_id')
#         new_booking.hotel_id = int(complete_id[complete_id.index('-')+1:])
#         new_booking.room_id = request.POST.get('room_type')
#         new_booking.save()
#         # update room details
#         rooms = Room.objects.filter(room_id=new_booking.room_id).order_by('room_no')[:int(new_booking.total_rooms)]
#         for room in rooms:
#             room.guest_id = new_booking.guest_id
#             room.room_status = 'B'
#             room.booking_id = new_booking.booking_id
#             room.save()
#         # send email confirmation
#         hotel_name = Hotel.objects.get(pk=new_booking.hotel_id).name
#         email_id = GuestDetails.objects.get(pk=new_booking.guest_id).email
#         email = EmailMessage('Booking confirmation', 'Your booking in ' + hotel_name + ' for room(s) of type ' +
#                              new_booking.room_id + ' on ' + new_booking.booking_date + ' has been confirmed.',
#                              to=[email_id])
#         email.send()
#         return redirect(reverse('summary') + '?booking_id={}'.format(new_booking.booking_id))
#     hotel_id = request.GET.get('hotel_id')
#     hotel_name = Hotel.objects.get(pk=hotel_id).name
#     records = Room.objects.filter(hotel_id=hotel_id)
#     room_types = [records[i].room_type for i in range(len(records))]
#     return render(request, 'new_booking.html', {'name': request.session['username'], 'room_types': room_types,
#                                                 'hotel_id': "bmh-"+str(hotel_id), 'hotel_name': hotel_name},
#                   RequestContext(request))

