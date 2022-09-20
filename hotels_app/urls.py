from django.urls import path
from hotels_app.views import HotelViewSet, RoomViewSet

urlpatterns = [
    path('', HotelViewSet.as_view({
        'get': 'list',
        'post': 'create'}),
         name='hotel-list'),
    path('rooms/', RoomViewSet.as_view({
        'get': 'list',
        'post': 'create'}),
         name='room-list'),
]
