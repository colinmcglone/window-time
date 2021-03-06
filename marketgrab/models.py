from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Data(models.Model):
    ticker = models.CharField(max_length=10)
    volume = models.DecimalField(max_digits=15, decimal_places=0)
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    aclose_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(editable=True, auto_now_add=False)
    def __str__(self):
        return self.ticker

class MovingAvg(models.Model):
    ticker = models.CharField(max_length=10)
    date = models.DateField(editable=True, auto_now_add=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    span = models.IntegerField()
    def __str__(self):
        return self.ticker

class Movements(models.Model):
    ticker = models.CharField(max_length=10)
    date = models.DateField(editable=True, auto_now_add=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    percent = models.FloatField()
    series = models.CharField(max_length=10)
    zvalue = models.FloatField()
    def __str__(self):
        return self.ticker

class Sigma(models.Model):
    ticker = models.CharField(max_length=10)
    date = models.DateField(editable=True, auto_now_add=False)
    series = models.CharField(max_length=10)
    value = models.FloatField()
