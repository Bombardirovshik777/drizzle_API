from time import sleep

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from drizzleAPP import models, serializers


class DrizzleApiView(APIView):

    def get(self, request, *args, **kwargs):
        weather_data = models.LeaderDrizzle.objects.filter(city=request.GET.get('city', None))
        # serializer = serializers.DrizzleSerializers(todos, many=True)
        return Response({}, status=status.HTTP_200_OK)


