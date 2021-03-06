# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-17 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_key_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rawpoint',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('payload', models.CharField(max_length=128)),
                ('rssi', models.IntegerField()),
                ('timestamp', models.DateTimeField(db_column=b'gw_timestamp')),
            ],
            options={
                'db_table': 'raw_data',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='gateway',
            name='gps_lat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='gateway',
            name='gps_lon',
            field=models.FloatField(default=0.0),
        ),
    ]
