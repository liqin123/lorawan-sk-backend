# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-04 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20160204_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='key',
            name='id',
        ),
        migrations.AlterField(
            model_name='key',
            name='numeric',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]