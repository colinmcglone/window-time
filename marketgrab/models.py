from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Quote(models.Model):
    ticker = models.CharField(max_length=10)
    quote_date = models.DateTimeField
    quote_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.ticker

class FiveDay(models.Model):
    ticker = models.CharField(max_length=10)
    avg_date = models.DateTimeField
    avg_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.ticker

class FiftyDay(models.Model):
    ticker = models.CharField(max_length=10)
    avg_date = models.DateTimeField
    avg_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.ticker

class TwoHundredDay(models.Model):
    ticker = models.CharField(max_length=10)
    avg_date = models.DateTimeField
    avg_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.ticker
