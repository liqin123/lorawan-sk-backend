# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-06 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0077_lorawanrawpoint_phypayload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lorawanrawpoint',
            name='FRMPayload',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
