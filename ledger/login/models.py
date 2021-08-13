from django.db import models

# Create your models here.
class Users(models.Model):
    userid = models.CharField(max_length=50)
    passw = models.CharField(max_length=50)
