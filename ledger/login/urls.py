

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login1, name='login1'),
    path('login', views.login1, name='login1'),
    path('checkpass', views.checkpass, name='checkpass')
]
