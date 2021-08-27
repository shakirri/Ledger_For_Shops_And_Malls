from django.db import models

# Create your models here.
class SalesTemp(models.Model):
    id = models.CharField(max_length=20, primary_key=True, serialize=False)
    name = models.CharField(max_length=50)
    amount=models.IntegerField()
    purchase_price=models.IntegerField()
    sale_price=models.IntegerField()
    per_total=models.IntegerField()
    

class Pricing(models.Model):
    id = models.CharField(max_length=20, primary_key=True, serialize=False)
    total_price=models.IntegerField()
    profit=models.IntegerField()