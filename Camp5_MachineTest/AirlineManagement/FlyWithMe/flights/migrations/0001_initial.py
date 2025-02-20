# Generated by Django 4.2.16 on 2024-09-18 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('FlightId', models.AutoField(primary_key=True, serialize=False)),
                ('DepAirport', models.CharField(max_length=50)),
                ('DepDate', models.DateField()),
                ('DepTime', models.TimeField()),
                ('ArrAirport', models.CharField(max_length=50)),
                ('ArrDate', models.DateField()),
                ('ArrTime', models.TimeField()),
            ],
        ),
    ]
