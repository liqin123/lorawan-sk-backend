# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-05 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_auto_20161005_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='lorawanrawpoint',
            name='gw',
            field=models.ForeignKey(blank=True, db_column=b'gw_serial', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Gateway'),
        ),
    ]