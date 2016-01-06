from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Data(models.Model):
    ticker = models.CharField(max_length=10)
    trading_day = models.CharField(max_length=10)
    volume = models.DecimalField(max_digits=15, decimal_places=0)
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    aclose_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.ticker

class FiveDay(models.Model):
    ticker = models.CharField(max_length=10)
    date = models.DateTimeField
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.ticker

class FiftyDay(models.Model):
    ticker = models.CharField(max_length=10)
    date = models.DateTimeField
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.ticker

class TwoHundredDay(models.Model):
    ticker = models.CharField(max_length=10)
    date = models.DateTimeField
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.ticker
