# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketgrab', '0006_data_daily_volume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='daily_volume',
        ),
        migrations.AddField(
            model_name='data',
            name='v',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
