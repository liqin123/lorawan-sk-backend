# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-02 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0087_auto_20161202_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gateway',
            name='description',
            field=models.TextField(),
        ),
    ]