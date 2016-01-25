from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the marketgrab index.")

def detail(request, ticker):
    return HttpResponse("You're looking at the details for %s." % ticker)

