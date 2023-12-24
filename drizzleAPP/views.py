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


# http://127.0.0.1:8000/whole_city_trunc/?city=spb
class WholeCityTrunc(APIView):

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
        for leader_data in weather_data.all():
            current_weather = {"t": leader_data.temp, "fl": leader_data.feels_like, "dp": leader_data.dew_point}
            if leader_data.precip_type != 0 and leader_data.precip_type is not None:
                current_weather['pt'] = leader_data.precip_type
            if leader_data.sub_type != 0 and leader_data.sub_type is not None:
                current_weather['st'] = leader_data.sub_type
            if leader_data.intensity != 0 and leader_data.intensity is not None:
                current_weather['i'] = leader_data.intensity
            if leader_data.prec_accum1 != 0 and leader_data.prec_accum1 is not None:
                current_weather['pa1'] = leader_data.prec_accum1
            if leader_data.prec_accum3 != 0 and leader_data.prec_accum3 is not None:
                current_weather['pa3'] = leader_data.prec_accum3
            if leader_data.prec_accum7 != 0 and leader_data.prec_accum7 is not None:
                current_weather['pa7'] = leader_data.prec_accum7
            if leader_data.precip_prob != 0 and leader_data.precip_prob is not None:
                current_weather['pp'] = leader_data.precip_prob
            if leader_data.weather_phenomena != 0 and leader_data.weather_phenomena is not None:
                current_weather['wf'] = leader_data.weather_phenomena
            if leader_data.cloudnes != 0 and leader_data.cloudnes is not None:
                current_weather['c'] = leader_data.cloudnes

            result['current_and_forecast'].append(
                [
                leader_data.lat,
                leader_data.lon,
                [
                    current_weather,
                    {'forecast'},
                    {'forecast'},
                ]
            ]
            )
        return Response(result, status=status.HTTP_200_OK)

# http://127.0.0.1:8000/whole_city_trunc_exp/?city=spb
class WholeCityTruncExp(APIView):

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
        for leader_data in weather_data.all():
            current_weather = {"temperature": leader_data.temp, "feels_lake": leader_data.feels_like,
                               "dew_point": leader_data.dew_point}
            if leader_data.precip_type != 0 and leader_data.precip_type is not None:
                current_weather['precip_type'] = leader_data.precip_type
            if leader_data.sub_type != 0 and leader_data.sub_type is not None:
                current_weather['sub_type'] = leader_data.sub_type
            if leader_data.intensity != 0 and leader_data.intensity is not None:
                current_weather['intensity'] = leader_data.intensity
            if leader_data.prec_accum1 != 0 and leader_data.prec_accum1 is not None:
                current_weather['precip_accumulate_1'] = leader_data.prec_accum1
            if leader_data.prec_accum3 != 0 and leader_data.prec_accum3 is not None:
                current_weather['precip_accumulate_3'] = leader_data.prec_accum3
            if leader_data.prec_accum7 != 0 and leader_data.prec_accum7 is not None:
                current_weather['precip_accumulate_7'] = leader_data.prec_accum7
            if leader_data.precip_prob != 0 and leader_data.precip_prob is not None:
                current_weather['precip_prob'] = leader_data.precip_prob
            if leader_data.weather_phenomena != 0 and leader_data.weather_phenomena is not None:
                current_weather['weather_phenomena'] = leader_data.weather_phenomena
            if leader_data.cloudnes != 0 and leader_data.cloudnes is not None:
                current_weather['cloudnes'] = leader_data.cloudnes

            result['current_and_forecast'].append(
                [
                    leader_data.lat,
                    leader_data.lon,
                    [
                        current_weather,
                        {'forecast'},
                        {'forecast'},
                    ]
                ]
            )
        return Response(result, status=status.HTTP_200_OK)

# http://127.0.0.1:8000/whole_city_full/?city=spb
class WholeCityFull(APIView):

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
        for leader_data in weather_data.all():
            current_weather = {"pt": leader_data.precip_type, "st": leader_data.sub_type, "i": leader_data.intensity,
                               "pa1": leader_data.prec_accum1, "pa3": leader_data.prec_accum3, "pa7": leader_data.prec_accum7,
                               "pp": leader_data.precip_prob, "wf": leader_data.weather_phenomena, "t": leader_data.temp,
                               "fl": leader_data.feels_like, "dp": leader_data.dew_point,"tmin": leader_data.temp_min,
                               "tmax": leader_data.temp_max, "c": leader_data.cloudnes}

            result['current_and_forecast'].append(
                [
                    leader_data.lat,
                    leader_data.lon,
                    [
                        current_weather,
                        {'forecast'},
                        {'forecast'},
                    ]
                ]
            )
        return Response(result, status=status.HTTP_200_OK)

# http://127.0.0.1:8000/whole_city_full_exp/?city=spb
class WholeCityFullExp(APIView):

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
        for leader_data in weather_data.all():
            current_weather = {"precip_type": leader_data.precip_type, "sub_type": leader_data.sub_type,
                               "intensity": leader_data.intensity, "precip_accumulate_1": leader_data.prec_accum1,
                               "precip_accumulate_3": leader_data.prec_accum3, "precip_accumulate_7": leader_data.prec_accum7,
                               "precip_prob": leader_data.precip_prob, "weather_phenomena": leader_data.weather_phenomena,
                               "temperature": leader_data.temp, "feels_lake": leader_data.feels_like,
                               "dew_point": leader_data.dew_point, "cloudnes": leader_data.cloudnes}

            result['current_and_forecast'].append(
                [
                    leader_data.lat,
                    leader_data.lon,
                    [
                        current_weather,
                        {'forecast'},
                        {'forecast'},
                    ]
                ]
            )
        return Response(result, status=status.HTTP_200_OK)

# http://127.0.0.1:8000/whole_city_full_exp_new/?city=spb
class WholeCityFullExp_new(APIView):

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
        for leader_data in weather_data.all():
            current_weather = {"precipitation": {"precip_type": leader_data.precip_type,
                                                 "sub_type": leader_data.sub_type,
                                                 "intensity": leader_data.intensity,
                                                 "precip_accumulate_1": leader_data.prec_accum1,
                                                 "precip_accumulate_3": leader_data.prec_accum3,
                                                 "precip_accumulate_7": leader_data.prec_accum7,
                                                 "precip_prob": leader_data.precip_prob
                                                 },
                               "phenomena": {
                                   "weather_phenomena": leader_data.weather_phenomena,
                               },
                               "main": {
                                   "temperature": leader_data.temp,
                                   "feels_lake": leader_data.feels_like,
                                   "dew_point": leader_data.dew_point,
                               },
                               "sky": {
                                   "cloudnes": leader_data.cloudnes
                               }
                               }

            result['current_and_forecast'].append(
                [
                    leader_data.lat,
                    leader_data.lon,
                    [
                        current_weather,
                        {'forecast'},
                        {'forecast'},
                    ]
                ]
            )
        return Response(result, status=status.HTTP_200_OK)









# http://127.0.0.1:8000/one_coordinate_trunc/?lat=60266439&lon=29783096
class OneCoordinateTrunc(APIView):

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
        leader_data = weather_data.first()
        if leader_data is None:
            return Response({'ERROR': 'no such coordinates'}, status=status.HTTP_400_BAD_REQUEST)
        current_weather = {"t": leader_data.temp, "fl": leader_data.feels_like, "dp": leader_data.dew_point}
        if leader_data.precip_type != 0 and leader_data.precip_type is not None:
            current_weather['pt'] = leader_data.precip_type
        if leader_data.sub_type != 0 and leader_data.sub_type is not None:
            current_weather['st'] = leader_data.sub_type
        if leader_data.intensity != 0 and leader_data.intensity is not None:
            current_weather['i'] = leader_data.intensity
        if leader_data.prec_accum1 != 0 and leader_data.prec_accum1 is not None:
            current_weather['pa1'] = leader_data.prec_accum1
        if leader_data.prec_accum3 != 0 and leader_data.prec_accum3 is not None:
            current_weather['pa3'] = leader_data.prec_accum3
        if leader_data.prec_accum7 != 0 and leader_data.prec_accum7 is not None:
            current_weather['pa7'] = leader_data.prec_accum7
        if leader_data.precip_prob != 0 and leader_data.precip_prob is not None:
            current_weather['pp'] = leader_data.precip_prob
        if leader_data.weather_phenomena != 0 and leader_data.weather_phenomena is not None:
            current_weather['wf'] = leader_data.weather_phenomena
        if leader_data.cloudnes != 0 and leader_data.cloudnes is not None:
            current_weather['c'] = leader_data.cloudnes
        result['current_and_forecast'].append([
            leader_data.lat,
            leader_data.lon,
            [
                current_weather,
                {'forecast'},
                {'forecast'},
            ]
        ]
        )
        return Response(result, status=status.HTTP_200_OK)

# http://127.0.0.1:8000/one_coordinate_trunc_exp/?lat=60266439&lon=29783096
class OneCoordinateTrunc_exp(APIView):

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
        leader_data = weather_data.first()
        if leader_data is None:
            return Response({'ERROR': 'no such coordinates'}, status=status.HTTP_400_BAD_REQUEST)
        current_weather = {"temperature": leader_data.temp, "feels_lake": leader_data.feels_like,
                           "dew_point": leader_data.dew_point}
        if leader_data.precip_type != 0 and leader_data.precip_type is not None:
            current_weather['precip_type'] = leader_data.precip_type
        if leader_data.sub_type != 0 and leader_data.sub_type is not None:
            current_weather['sub_type'] = leader_data.sub_type
        if leader_data.intensity != 0 and leader_data.intensity is not None:
            current_weather['intensity'] = leader_data.intensity
        if leader_data.prec_accum1 != 0 and leader_data.prec_accum1 is not None:
            current_weather['precip_accumulate_1'] = leader_data.prec_accum1
        if leader_data.prec_accum3 != 0 and leader_data.prec_accum3 is not None:
            current_weather['precip_accumulate_3'] = leader_data.prec_accum3
        if leader_data.prec_accum7 != 0 and leader_data.prec_accum7 is not None:
            current_weather['precip_accumulate_7'] = leader_data.prec_accum7
        if leader_data.precip_prob != 0 and leader_data.precip_prob is not None:
            current_weather['precip_prob'] = leader_data.precip_prob
        if leader_data.weather_phenomena != 0 and leader_data.weather_phenomena is not None:
            current_weather['weather_phenomena'] = leader_data.weather_phenomena
        if leader_data.cloudnes != 0 and leader_data.cloudnes is not None:
            current_weather['cloudnes'] = leader_data.cloudnes
        result['current_and_forecast'].append([
            leader_data.lat,
            leader_data.lon,
            [
                current_weather,
                {'forecast'},
                {'forecast'},
            ]
        ]
        )
        return Response(result, status=status.HTTP_200_OK)


# http://127.0.0.1:8000/one_coordinate_full/?lat=60266439&lon=29783096
class OneCoordinateFull(APIView):

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
        leader_data = weather_data.first()
        if leader_data is None:
            return Response({'ERROR': 'no such coordinates'}, status=status.HTTP_400_BAD_REQUEST)
        current_weather = {"pt": leader_data.precip_type, "st": leader_data.sub_type, "i": leader_data.intensity,
                           "pa1": leader_data.prec_accum1, "pa3": leader_data.prec_accum3, "pa7": leader_data.prec_accum7,
                           "pp": leader_data.precip_prob, "wf": leader_data.weather_phenomena, "t": leader_data.temp,
                           "fl": leader_data.feels_like, "dp": leader_data.dew_point,"tmin": leader_data.temp_min,
                           "tmax": leader_data.temp_max, "c": leader_data.cloudnes}
        result['current_and_forecast'].append([
            leader_data.lat,
            leader_data.lon,
            [
                current_weather,
                {'forecast'},
                {'forecast'},
            ]
        ]
        )
        return Response(result, status=status.HTTP_200_OK)

# http://127.0.0.1:8000/one_coordinate_full_exp/?lat=60266439&lon=29783096
class OneCoordinateFull_exp(APIView):

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
        leader_data = weather_data.first()
        if leader_data is None:
            return Response({'ERROR': 'no such coordinates'}, status=status.HTTP_400_BAD_REQUEST)
        current_weather = {"precip_type": leader_data.precip_type, "sub_type": leader_data.sub_type,
                           "intensity": leader_data.intensity, "precip_accumulate_1": leader_data.prec_accum1,
                           "precip_accumulate_3": leader_data.prec_accum3, "precip_accumulate_7": leader_data.prec_accum7,
                           "precip_prob": leader_data.precip_prob, "weather_phenomena": leader_data.weather_phenomena,
                           "temperature": leader_data.temp, "feels_lake": leader_data.feels_like,
                           "dew_point": leader_data.dew_point, "temperature_min":leader_data.temp_min,
                           "temperature_max": leader_data.temp_max, "cloudnes": leader_data.cloudnes}
        result['current_and_forecast'].append([
            leader_data.lat,
            leader_data.lon,
            [
                current_weather,
                {'forecast'},
                {'forecast'},
            ]
        ]
        )
        return Response(result, status=status.HTTP_200_OK)

# http://127.0.0.1:8000/one_coordinate_full_exp_new/?lat=60266439&lon=29783096
class OneCoordinateFull_exp_new(APIView):

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
        leader_data = weather_data.first()
        if leader_data is None:
            return Response({'ERROR': 'no such coordinates'}, status=status.HTTP_400_BAD_REQUEST)
        current_weather = {"precipitation": {"precip_type": leader_data.precip_type,
                                             "sub_type": leader_data.sub_type,
                                             "intensity": leader_data.intensity,
                                             "precip_accumulate_1": leader_data.prec_accum1,
                                             "precip_accumulate_3": leader_data.prec_accum3,
                                             "precip_accumulate_7": leader_data.prec_accum7,
                                             "precip_prob": leader_data.precip_prob
                                             },
                           "phenomena": {
                               "weather_phenomena": leader_data.weather_phenomena,
                           },
                           "main": {
                               "temperature": leader_data.temp,
                               "feels_lake": leader_data.feels_like,
                               "dew_point": leader_data.dew_point,
                               "temperature_min":leader_data.temp_min,
                               "temperature_max": leader_data.temp_max
                           },
                           "sky": {
                               "cloudnes": leader_data.cloudnes
                           }
                           }
        result['current_and_forecast'].append([
            leader_data.lat,
            leader_data.lon,
            [
                current_weather,
                {'forecast'},
                {'forecast'},
            ]
        ]
        )
        return Response(result, status=status.HTTP_200_OK)










class GroupCoordinateTrunc(APIView):

    def get(self, request: WSGIRequest, *args, **kwargs):
        params = json.loads(request.body)
        result = {
           'current_and_forecast': [],
           'errors': []
       }
        for coord in params['coordinates']:
            if 'lat' not in coord.keys() or 'lon' not in coord.keys():
                result['errors'].append({'message': 'you must pass lat and lon keys',
                                         'data': coord})
            else:
                lat = str(coord['lat']).replace('.', '')
                lon = str(coord['lon']).replace('.', '')
                try:
                    weather_data = cache.filter(lat=lat, lon=lon)
                except ValueError:
                    result['errors'].append({'message': 'coordinate must be numbers',
                                             'data': coord})
                    continue
                leader_data = weather_data.first()
                if leader_data is None:
                    result['errors'].append({'message': 'no such coordinates',
                                             'data': coord})
                    continue
                current_weather = {"t": leader_data.temp, "fl": leader_data.feels_like, "dp": leader_data.dew_point}
                if leader_data.precip_type != 0 and leader_data.precip_type is not None:
                    current_weather['pt'] = leader_data.precip_type
                if leader_data.sub_type != 0 and leader_data.sub_type is not None:
                    current_weather['st'] = leader_data.sub_type
                if leader_data.intensity != 0 and leader_data.intensity is not None:
                    current_weather['i'] = leader_data.intensity
                if leader_data.prec_accum1 != 0 and leader_data.prec_accum1 is not None:
                    current_weather['pa1'] = leader_data.prec_accum1
                if leader_data.prec_accum3 != 0 and leader_data.prec_accum3 is not None:
                    current_weather['pa3'] = leader_data.prec_accum3
                if leader_data.prec_accum7 != 0 and leader_data.prec_accum7 is not None:
                    current_weather['pa7'] = leader_data.prec_accum7
                if leader_data.precip_prob != 0 and leader_data.precip_prob is not None:
                    current_weather['pp'] = leader_data.precip_prob
                if leader_data.weather_phenomena != 0 and leader_data.weather_phenomena is not None:
                    current_weather['wf'] = leader_data.weather_phenomena
                if leader_data.cloudnes != 0 and leader_data.cloudnes is not None:
                    current_weather['s'] = leader_data.cloudnes
                result['current_and_forecast'].append(
                    [
                    leader_data.lat,
                    leader_data.lon,
                    [
                        current_weather,
                        {'forecast'},
                        {'forecast'},
                    ]
                ]
                )
        return Response(result, status=status.HTTP_200_OK)


class GroupCoordinateFull(APIView):

    def get(self, request: WSGIRequest, *args, **kwargs):
        params = json.loads(request.body)
        result = {
            'current_and_forecast': [],
            'errors': []
        }
        for coord in params['coordinates']:
            if 'lat' not in coord.keys() or 'lon' not in coord.keys():
                result['errors'].append({'message': 'you must pass lat and lon keys',
                                         'data': coord})
            else:
                lat = str(coord['lat']).replace('.', '')
                lon = str(coord['lon']).replace('.', '')
                try:
                    weather_data = cache.filter(lat=lat, lon=lon)
                except ValueError:
                    result['errors'].append({'message': 'coordinate must be numbers',
                                             'data': coord})
                    continue
                leader_data = weather_data.first()
                if leader_data is None:
                    result['errors'].append({'message': 'no such coordinates',
                                             'data': coord})
                    continue
                current_weather = {"t": leader_data.temp, "fl": leader_data.feels_like, "dp": leader_data.dew_point}
                if leader_data.precip_type != 0 and leader_data.precip_type is not None:
                    current_weather['pt'] = leader_data.precip_type
                if leader_data.sub_type != 0 and leader_data.sub_type is not None:
                    current_weather['st'] = leader_data.sub_type
                if leader_data.intensity != 0 and leader_data.intensity is not None:
                    current_weather['i'] = leader_data.intensity
                if leader_data.prec_accum1 != 0 and leader_data.prec_accum1 is not None:
                    current_weather['pa1'] = leader_data.prec_accum1
                if leader_data.prec_accum3 != 0 and leader_data.prec_accum3 is not None:
                    current_weather['pa3'] = leader_data.prec_accum3
                if leader_data.prec_accum7 != 0 and leader_data.prec_accum7 is not None:
                    current_weather['pa7'] = leader_data.prec_accum7
                if leader_data.precip_prob != 0 and leader_data.precip_prob is not None:
                    current_weather['pp'] = leader_data.precip_prob
                if leader_data.weather_phenomena != 0 and leader_data.weather_phenomena is not None:
                    current_weather['wf'] = leader_data.weather_phenomena
                if leader_data.cloudnes != 0 and leader_data.cloudnes is not None:
                    current_weather['s'] = leader_data.cloudnes
                result['current_and_forecast'].append(
                    [
                        leader_data.lat,
                        leader_data.lon,
                        [
                            current_weather,
                            {'forecast'},
                            {'forecast'},
                        ]
                    ]
                )
        return Response(result, status=status.HTTP_200_OK)





