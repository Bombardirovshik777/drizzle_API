# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CheckWxMetar(models.Model):
    resp_check_metar = models.JSONField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    location_api = models.CharField(max_length=30, blank=True, null=True)
    location_driz = models.CharField(max_length=30, blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'check_wx_metar'


class ForecaResponseCurrent(models.Model):
    resp_foreca = models.JSONField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    utc_time = models.DateTimeField(blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)
    location_api = models.CharField(max_length=100, blank=True, null=True)
    location_driz = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foreca_response_current'


class LeaderDrizzle(models.Model):
    lat = models.BigIntegerField(blank=True, null=True)
    lon = models.BigIntegerField(blank=True, null=True)
    updated_local_time = models.DateTimeField(blank=True, null=True)
    unix_time = models.DateTimeField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)  # This field type is a guess.
    precip_type = models.SmallIntegerField(blank=True, null=True)
    sub_type = models.SmallIntegerField(blank=True, null=True)
    intensity = models.SmallIntegerField(blank=True, null=True)
    prec_accum1 = models.FloatField(blank=True, null=True)
    prec_accum3 = models.FloatField(blank=True, null=True)
    prec_accum7 = models.FloatField(blank=True, null=True)
    precip_prob = models.FloatField(blank=True, null=True)
    weather_phenomena = models.SmallIntegerField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    feels_like = models.FloatField(blank=True, null=True)
    temp_min = models.FloatField(blank=True, null=True)
    temp_max = models.FloatField(blank=True, null=True)
    dew_point = models.FloatField(blank=True, null=True)
    cloudnes = models.FloatField(blank=True, null=True)
    polygon = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leader_drizzle'


class MetsouResponseCurrent(models.Model):
    resp_metsou = models.JSONField()
    created_time = models.DateTimeField()
    utc_time = models.DateTimeField()
    timezone = models.CharField(max_length=30, blank=True, null=True)
    location_api = models.CharField(max_length=100, blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)
    location_driz = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metsou_response_current'


class MtcomMetarResponseCurrent(models.Model):
    resp_mtcom_metar = models.JSONField()
    created_time = models.DateTimeField()
    utc_time = models.DateTimeField()
    location_driz = models.CharField(max_length=100, blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtcom_metar_response_current'


class NinjasRespCurr(models.Model):
    resp_ninjas = models.JSONField()
    created_time = models.DateTimeField()
    utc_time = models.DateTimeField()
    location_api = models.CharField(max_length=100, blank=True, null=True)
    location_driz = models.CharField(max_length=100, blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ninjas_resp_curr'


class OikoRespCurr(models.Model):
    resp_oiko = models.JSONField()
    created_time = models.DateTimeField()
    location_driz = models.CharField(max_length=100, blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)
    utc_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oiko_resp_curr'


class OpenMRespCurr(models.Model):
    resp_open_m = models.JSONField()
    created_time = models.DateTimeField()
    utc_time = models.DateTimeField()
    location_api = models.CharField(max_length=100, blank=True, null=True)
    location_driz = models.CharField(max_length=100, blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_m_resp_curr'


class OwmResponseCurrent(models.Model):
    resp_owm = models.JSONField()
    created_time = models.DateTimeField()
    utc_time = models.DateTimeField()
    timezone = models.SmallIntegerField()
    location_api = models.CharField(max_length=100, blank=True, null=True)
    location_driz = models.CharField(max_length=100, blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'owm_response_current'


class SandboxDrizzle(models.Model):
    temp = models.FloatField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    feels_like = models.FloatField(blank=True, null=True)
    cloudnes = models.FloatField(blank=True, null=True)
    precip_prob = models.FloatField(blank=True, null=True)
    precip_type = models.SmallIntegerField(blank=True, null=True)
    intensity = models.SmallIntegerField(blank=True, null=True)
    prec_accum1 = models.FloatField(blank=True, null=True)
    prec_accum3 = models.FloatField(blank=True, null=True)
    prec_accum7 = models.FloatField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)
    wind_gust = models.FloatField(blank=True, null=True)
    obs_time = models.BigIntegerField(blank=True, null=True)
    state_summary = models.SmallIntegerField(blank=True, null=True)
    utc_time = models.DateTimeField(blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)
    dew_point = models.FloatField(blank=True, null=True)
    temp_min = models.FloatField(blank=True, null=True)
    temp_max = models.FloatField(blank=True, null=True)
    sub_type = models.IntegerField(blank=True, null=True)
    lat = models.IntegerField(blank=True, null=True)
    lon = models.IntegerField(blank=True, null=True)
    weather_phenomena = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sandbox_drizzle'


class StormglassResponseCurrent(models.Model):
    resp_stormg = models.JSONField()
    created_time = models.DateTimeField()
    utc_time = models.DateTimeField()
    timezone = models.SmallIntegerField()
    location_api = models.CharField(max_length=100, blank=True, null=True)
    location_driz = models.CharField(max_length=100, blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stormglass_response_current'


class TomorrowResponseCurrent(models.Model):
    resp_tomorr = models.JSONField()
    created_time = models.DateTimeField()
    utc_time = models.DateTimeField()
    location_api = models.CharField(max_length=100, blank=True, null=True)
    location_driz = models.CharField(max_length=100, blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tomorrow_response_current'


class VisualcrossingResponseCurrent(models.Model):
    resp_visualcrossing = models.JSONField()
    created_time = models.DateTimeField()
    utc_time = models.DateTimeField()
    location_api = models.CharField(max_length=100, blank=True, null=True)
    location_driz = models.CharField(max_length=100, blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visualcrossing_response_current'


class WbitResponseCurrent(models.Model):
    resp_wbit = models.JSONField()
    created_time = models.DateTimeField()
    utc_time = models.DateTimeField()
    timezone = models.SmallIntegerField()
    location = models.CharField(max_length=100, blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wbit_response_current'


class WeatherApiResponseCurrent(models.Model):
    resp_we_api = models.JSONField()
    created_time = models.DateTimeField()
    utc_time = models.DateTimeField()
    location_api = models.CharField(max_length=100, blank=True, null=True)
    location_driz = models.CharField(max_length=100, blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_api_response_current'


class WeatherstackRespCurr(models.Model):
    resp_ws = models.JSONField()
    created_time = models.DateTimeField()
    utc_time = models.DateTimeField()
    timezone = models.CharField(max_length=35)
    location_api = models.CharField(max_length=100)
    unix_time = models.IntegerField(blank=True, null=True)
    location_driz = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weatherstack_resp_curr'


class WindyResponseCurrent(models.Model):
    resp_windy = models.JSONField()
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'windy_response_current'


class WwoResponseCurrent(models.Model):
    resp_wwo = models.JSONField()
    created_time = models.DateTimeField()
    utc_time = models.DateTimeField()
    location_api = models.CharField(max_length=100, blank=True, null=True)
    location_driz = models.CharField(max_length=100, blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wwo_response_current'


class YadResponseCurrent(models.Model):
    resp_yad = models.JSONField()
    created_time = models.DateTimeField()
    utc_time = models.DateTimeField()
    timezone = models.SmallIntegerField()
    location_api = models.CharField(max_length=100)
    location_driz = models.CharField(max_length=100, blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yad_response_current'



class WeatherPhenomenaTable(models.Model):
    code = models.IntegerField(null=False, unique=True, verbose_name='weather_phenomena_code', help_text='777')
    description = models.CharField(max_length=250)
    abbreviation = models.CharField(max_length=250)
    text = models.CharField(max_length=250)

    class Meta:
        db_table = 'weather_phenomena_sum'

    def __str__(self):
        return f'{self.code} {self.description}'
