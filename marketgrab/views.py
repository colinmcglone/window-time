import os
from django.conf import *
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from .models import Data, MovingAvg, Movements, Sigma
from datetime import datetime
from django.template import RequestContext

def index(request):

    ticker = Data.objects.values_list('ticker').distinct()
    market = []
    for t in ticker:
        t = t[0]

        price = Data.objects.filter(ticker=t).latest('date').aclose_price
        date = Data.objects.filter(ticker=t).latest('date').date

        move_price = Movements.objects.filter(ticker=t, series='market').latest('date').price
        move_percent = Movements.objects.filter(ticker=t, series='market').latest('date').percent
        move_zscore = Movements.objects.filter(ticker=t, series='market').latest('date').zvalue
        spans = MovingAvg.objects.values_list('span').distinct()

        i = {
            'index':t,
            'price':price,
            'date':date,
            'move_price':move_price,
            'move_percent':round(move_percent, 4),
            'move_zscore':round(move_zscore, 4),
            'hist':'marketgrab/'+t+'_hist.png'
            }

        market.append(i)

        for s in spans:
            s = s[0]

            avg_price = Movements.objects.filter(ticker=t, series=s).latest('date').price
            avg_percent = Movements.objects.filter(ticker=t, series=s).latest('date').percent
            zscore = Movements.objects.filter(ticker=t, series=s).latest('date').zvalue

            a = {
                'ticker':t,
                'span':s,
                'price':avg_price,
                'percent':round(avg_percent, 4),
                'zscore':round(zscore, 4)
                }

            (item for item in market if item['index']==t).next()[str(s) + '_avg'] = a


    context = RequestContext(request, {'market':market})

    return render_to_response('marketgrab/index.html', context_instance = context)

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
