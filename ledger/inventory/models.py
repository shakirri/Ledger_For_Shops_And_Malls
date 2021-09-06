from django.db import models

# Create your models here.
class Products(models.Model):
    id = models.CharField(max_length=20, primary_key=True, serialize=False)
    name = models.CharField(max_length=50)
    amount=models.IntegerField()
    purchase_price=models.IntegerField()
    sale_price=models.IntegerField()

class Assets(models.Model):
    id = models.CharField(max_length=20, primary_key=True, serialize=False)
    cash = models.IntegerField()
    profit = models.IntegerField()
    inventory_value = models.IntegerField()
    total_sales = models.IntegerField()
    total_purchases = models.IntegerField()