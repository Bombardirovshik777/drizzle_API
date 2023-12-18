from django.urls import path
from rest_framework import routers
from drizzleAPP import views


router = routers.DefaultRouter()

urlpatterns = [
    path('full_city/', views.FullCity.as_view(), name='full_city'),
    path('one_coordinate/', views.OneCoordinate.as_view(), name='one_coordinate'),
]