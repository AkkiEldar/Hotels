from django.urls import path
from authentication_app.views import AccountRegisterAPIViews, LoginView


urlpatterns = [
    path('registration/', AccountRegisterAPIViews.as_view(), name='user-registration'),
    path('', LoginView.as_view())
]
