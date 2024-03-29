

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addprod', views.addprod, name='addprod'),
    path('purchased', views.purchased, name='purchased'),
    path('newprod', views.newprod, name='newprod'),
    path('oldprod', views.oldprod, name='oldprod'),
    path('oldpurchased', views.oldpurchased, name='oldpurchased'),
    path('check_inv', views.check_inv, name='check_inv'),
    path('home', views.home, name='home'),
    path('sell', views.sell, name='sell'),
    path('addsales', views.addsales, name='addsales'),
    path('sold', views.sold, name='sold'),
    path('balance', views.balance, name='balance'),
]