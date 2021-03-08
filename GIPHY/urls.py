from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url( r'^listing', views.listing),
    #url( r'^search', views.search),
    url( r'^(?P<tag>[\w]+)/$', views.search),
]