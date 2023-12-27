# Generated by Django 5.0 on 2023-12-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drizzleAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherPhenomenaTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(help_text='777', unique=True, verbose_name='weather_phenomena_code')),
                ('description', models.CharField(max_length=250)),
                ('abbreviation', models.CharField(max_length=250)),
                ('text', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'weather_phenomena_sum',
            },
        ),
    ]
