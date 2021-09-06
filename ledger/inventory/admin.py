from django.contrib import admin
from .models import Assets, Products

# Register your models here.

admin.site.register(Products)
admin.site.register(Assets)