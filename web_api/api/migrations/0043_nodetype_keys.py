# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-04 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_auto_20160904_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodetype',
            name='keys',
            field=models.ManyToManyField(to='api.Key'),
        ),
    ]
