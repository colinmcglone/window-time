from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Data

def index(request):
    t = get_template('index.html')
    ticker = Data.objects.values('ticker').distinct()
    return HttpResponse(t.render(ticker, request))

def detail(request, t):
    if Data.objects.filter(ticker=t).exists():
        response = "You're looking at the details for %s."

    else:
        response = "Sorry, cannot find data for %s."

    return HttpResponse(response % t)
