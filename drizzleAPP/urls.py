from django.urls import path
from rest_framework import routers
from drizzleAPP import views


router = routers.DefaultRouter()

urlpatterns = [
    # CITY
    path('whole_city_trunc/', views.WholeCityTrunc.as_view(), name='whole_city_trunc'),
    path('whole_city_trunc_exp/', views.WholeCityTruncExp.as_view(), name='whole_city_trunc_exp'),

    path('whole_city_full/', views.WholeCityFull.as_view(), name='whole_city_full'),
    path('whole_city_full_exp/', views.WholeCityFullExp.as_view(), name='whole_city_full_exp'),
    path('whole_city_full_exp_new/', views.WholeCityFullExp_new.as_view(), name='whole_city_full_exp_new'),




    # ONE
    path('one_coordinate_trunc/', views.OneCoordinateTrunc.as_view(), name='one_coordinate_trunc'),
    path('one_coordinate_trunc_exp/', views.OneCoordinateTrunc_exp.as_view(), name='one_coordinate_trunc_exp'),


    path('one_coordinate_full/', views.OneCoordinateFull.as_view(), name='one_coordinate_full'),
    path('one_coordinate_full_exp/', views.OneCoordinateFull_exp.as_view(), name='one_coordinate_full_exp'),

    path('one_coordinate_full_exp_new/', views.OneCoordinateFull_exp_new.as_view(), name='one_coordinate_full_exp_new'),




    # GROUP
    path('group_coordinate_trunc/', views.GroupCoordinateTrunc.as_view(), name='group_coordinate_trunc'),
    path('group_coordinate_full/', views.GroupCoordinateFull.as_view(), name='group_coordinate_full'),

]


