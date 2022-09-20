from django.test import TestCase, Client
from django.contrib.auth.models import User
from hotels_app.models import Hotel


# class TestHotelCreate(TestCase):
#     def test_should_create_hotel(self):
#         c = Client()
#         response = c.post(
#             'http://127.0.0.1:8000/hotel/',
#             data={
#                 'name': 'test hotel 1',
#                 'location': 'https://www.youtube.com/watch?v=M6iTV-ZdjP4',
#                 'description': 'sldnviabwes skvn',
#                 'contact': 'sdmvlenolds@mail.ru',
#                 'rooms_count': '120',
#                 'star': '4'
#             }
#         )
#         # print(response.status_code)
#         assert response.status_code == 201


# class TestRoomCreate(TestCase):
#     def test_should_create_room(self):
#         c = Client
#         response = c.post(
#             'http://127.0.0.1:8000/hotel/rooms/',
#             data={
#                 'floor': '2',
#                 'room_number': '69',
#                 'is_active': 'True',
#                 'room_type': 'luxe',
#                 'price': '6900',
#                 'rooms': '6',
#                 'description': 'что то по питонски',
#                 'how_mach_people': '9',
#                 'hotel': '1',
#             }
#         )
#         # print(response.status_code)
#         assert response.status_code == 201
