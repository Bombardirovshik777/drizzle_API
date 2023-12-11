from django.urls import path
from rest_framework import routers
from drizzleAPP import views


router = routers.DefaultRouter()

urlpatterns = [
    path('all_weather/', views.DrizzleApiView.as_view(), name='Список всех погодных условий'),
]