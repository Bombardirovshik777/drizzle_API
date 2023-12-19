import json
from time import sleep

from django.core.handlers.wsgi import WSGIRequest
from django.db import DataError

from .jobs import cache

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from drizzleAPP import models, serializers


class FullCity(APIView):

    def get(self, request: WSGIRequest, *args, **kwargs):
        # weather_data = models.LeaderDrizzle.objects.filter(city=request.GET.get('city', None))
        city = request.GET.get('city', None)
        if not city: return Response({'ERROR': f'missing "city" parameter, got {request.build_absolute_uri("/")}{request.get_full_path()[1:]}?city=you_city'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            weather_data = cache.filter(city=city)
        except DataError: return Response({'ERROR': 'city is not found'}, status=status.HTTP_204_NO_CONTENT)
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
            result['current_and_forecast'].append(
                [
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

    def get(self, request: WSGIRequest, *args, **kwargs):
        lat = request.GET.get('lat', None)
        if lat: lat = lat.replace('.', '')
        else: return Response({'ERROR': 'error in lat'}, status=status.HTTP_400_BAD_REQUEST)
        lon = request.GET.get('lon', None).replace('.', '')
        if lon: lon = lon.replace('.', '')
        else: return Response({'ERROR': 'error in lon'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            weather_data = cache.filter(lat=lat, lon=lon)
        except ValueError: return Response({'ERROR' : 'coordinate must be numbers'}, status=status.HTTP_400_BAD_REQUEST)
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


class GroupCoordinate(APIView):

    def get(self, request: WSGIRequest, *args, **kwargs):
        params = json.loads(request.body)
        result = {
           'current_and_forecast': [],
           'errors': []
       }
        for coord in params['coordinates']:
            if 'lat' not in coord.keys() or 'lon' not in coord.keys():
                result['errors'].append(coord)
            else:
                lat = coord['lat'].replace('.', '')
                lon = coord['lon'].replace('.', '')
                try:
                    weather_data = cache.filter(lat=lat, lon=lon)
                except ValueError: return Response({'ERROR' : 'coordinate must be numbers'}, status=status.HTTP_400_BAD_REQUEST)
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
                result['current_and_forecast'].append(
                    [
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




