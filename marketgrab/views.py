import os
from django.conf import *
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Data, MovingAvg, Movements, Sigma
from datetime import datetime


def index(request):
    markets = []
    ticker = Data.objects.values_list('ticker').distinct()
    for index in ticker:
        index = index[0]
        market = Data.objects.filter(ticker=index).latest('date')
        move = Movements.objects.filter(ticker=index, series='market').latest('date')
        sig = Significance.objects.filter(ticker=index, series='market').latest('date')

        avgs = MovingAvg.objects.filter(ticker=index).values_list('span').distinct()
        spans = []
        for span in avgs:
            avgmove = Movements.objects.filter(ticker=index, series=span),latest('date')
            avgsig = Significance.objects.filter(ticker=index, series=span).latest('date')
            spans.extend[span, avgmove.price, avgmove.percent, avgsig.value]

        markets.extend([index, market.price, market.date, move.price, move.percent, sig.value, spans])

        return HttpResponse("%s" % markets)


def detail(request, t):
    if Data.objects.filter(ticker=t).exists():
        response = "You're looking at the details for %s."

    else:
        response = "Sorry, cannot find data for %s."

    return HttpResponse(response % t)

def graphs(request):
    path = os.path.abspath(os.path.join(settings.BASE_DIR, '..', 'public/static/marketgrab'))
    images = []
    for f in os.listdir(path):
        if f.endswith("png"):
            images.append("marketgrab/%s" % f)
    context = {'images': images}
    return render(request, 'marketgrab/graphs.html', context)
