# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketgrab', '0004_remove_data_aclose_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='aclose_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
