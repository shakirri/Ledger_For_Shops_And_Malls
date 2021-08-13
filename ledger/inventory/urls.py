

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addprod', views.addprod, name='addprod'),
    path('purchased', views.purchased, name='purchased'),
    path('newprod', views.newprod, name='newprod'),
    path('oldprod', views.oldprod, name='oldprod'),
    path('oldpurchased', views.oldpurchased, name='oldpurchased'),
]
