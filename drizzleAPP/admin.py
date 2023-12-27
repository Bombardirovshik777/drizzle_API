from django.contrib import admin
from .models import WeatherPhenomenaTable


@admin.register(WeatherPhenomenaTable)
class WeatherPhenomenaTableAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'description')
