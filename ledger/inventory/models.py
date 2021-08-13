from django.db import models

# Create your models here.
class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    amount=models.IntegerField()
    purchase_price=models.IntegerField()
    sale_price=models.IntegerField()
