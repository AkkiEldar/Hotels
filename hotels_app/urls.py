from django.urls import path
from hotels_app.views import HotelViewSet, RoomViewSet

urlpatterns = [
    path('hotels/', HotelViewSet.as_view({'get': 'list'}), name='hotel-list'),
    path('rooms/', RoomViewSet.as_view({'get': 'list'}), name='room-list'),
]
