# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-05 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketgrab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('open_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('low_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('close_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('aclose_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Quote',
        ),
        migrations.RenameField(
            model_name='fiftyday',
            old_name='avg_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='fiveday',
            old_name='avg_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='twohundredday',
            old_name='avg_price',
            new_name='price',
        ),
    ]
