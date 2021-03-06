# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-08 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketgrab', '0013_remove_data_trading_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovingAvg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='FiftyDay',
        ),
        migrations.DeleteModel(
            name='FiveDay',
        ),
        migrations.DeleteModel(
            name='TwoHundredDay',
        ),
    ]
