from time import sleep
from .jobs import cache

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from drizzleAPP import models, serializers


class FullCity(APIView):

    def get(self, request, *args, **kwargs):
        # weather_data = models.LeaderDrizzle.objects.filter(city=request.GET.get('city', None))
        weather_data = cache.filter(city=request.GET.get('city', None))
        result = {
            'current_and_forecast': []
        }
        for raw in weather_data.all():
            current_weather = {}
            if raw.precip_type != 0 and raw.precip_type is not None:
                current_weather['pt'] = raw.precip_type
            if raw.sub_type != 0 and raw.sub_type is not None:
                current_weather['st'] = raw.sub_type
            if raw.intensity != 0 and raw.intensity is not None:
                current_weather['i'] = raw.intensity
            result['current_and_forecast'].append([
                raw.lat,
                raw.lon,
                [
                    current_weather,
                    {'forecast'},
                    {'forecast'},
                ]
            ]
            )



        return Response(result, status=status.HTTP_200_OK)

class OneCoordinate(APIView):

    def get(self, request, *args, **kwargs):
        # weather_data = models.LeaderDrizzle.objects.filter(city=request.GET.get('city', None))
        lat = request.GET.get('lat', None)
        if lat: lat = lat.replace('.', '')
        else: return Response({'ERROR': 'error in lat'}, status=status.HTTP_400_BAD_REQUEST)
        lon = request.GET.get('lon', None).replace('.', '')
        weather_data = cache.filter(lat=lat, lon=lon)
        result = {
            'current_and_forecast': []
        }
        print(request.GET)
        raw = weather_data.first()
        if raw is None:
            return Response({'ERROR': 'coord none'}, status=status.HTTP_400_BAD_REQUEST)
        current_weather = {}
        if raw.precip_type != 0 and raw.precip_type is not None:
            current_weather['pt'] = raw.precip_type
        if raw.sub_type != 0 and raw.sub_type is not None:
            current_weather['st'] = raw.sub_type
        if raw.intensity != 0 and raw.intensity is not None:
            current_weather['i'] = raw.intensity
        result['current_and_forecast'].append([
            raw.lat,
            raw.lon,
            [
                current_weather,
                {'forecast'},
                {'forecast'},
            ]
        ]
        )



        return Response(result, status=status.HTTP_200_OK)


    # http://127.0.0.1:8000/one_coordinate/?lat=59775907&lon=30667645



