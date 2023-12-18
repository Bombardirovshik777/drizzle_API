from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from drizzleAPP import models, serializers


cache = models.LeaderDrizzle.objects.all()


def update_cache():
    global cache
    while True:
        print('updating cache...')
        cache = models.LeaderDrizzle.objects.all()
        sleep(2)

# Create your views here.
class DrizzleApiView(APIView):

    def get(self, request, *args, **kwargs):
        weather_data = models.LeaderDrizzle.objects.filter(city=request.GET.get('city', None))
        # serializer = serializers.DrizzleSerializers(todos, many=True)
        return Response({}, status=status.HTTP_200_OK)


