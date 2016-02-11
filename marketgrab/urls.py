from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^analysis/graphs/$', views.graphs),
    url(r'^ticker/(?P<t>[A-Za-z]+)/$', views.detail),
]
