# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-04 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0091_auto_20161202_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='gateway',
            name='last_seen',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
