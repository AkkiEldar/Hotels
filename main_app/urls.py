from django.urls import path
from main_app.views import InfoViewSet, OurPartnersViewSet, AboutUsViewSet
# RecomendationHotelsViewSet,
urlpatterns = [
    # path('', RecomendationHotelsViewSet.as_view({'get': 'list'}), name='recomendation-list'),
    path('', InfoViewSet.as_view({'get': 'list'}), name='info-list'),
    path('our-partners/', OurPartnersViewSet.as_view({'get': 'list'}), name='partners-list'),
    path('about-us/', AboutUsViewSet.as_view({'get': 'list'}), name='about-us-list')
]
