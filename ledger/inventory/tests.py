from django.test import TestCase, Client
from django.test import SimpleTestCase
from .models import Products, Assets
from django.urls import reverse, resolve
from .views import addprod, purchased, oldprod, newprod, oldpurchased, check_inv, home, addsales, sell, sold, balance

# Create your tests here.

class Test_Models(TestCase):
    def test_fields_products(self):
        pr=Products()
        pr.id="1"
        pr.name="Football"
        pr.amount=30
        pr.purchase_price=15
        pr.sale_price=20
        pr.save()

        record=Products.objects.get(id=1)
        self.assertEqual(record, pr)

    def test_fields_assets(self):
        a=Assets()
        a.id="1"
        a.cash=10000
        a.profit=300
        a.inventory_value=3000
        a.total_purchases=1500
        a.total_sales=2000
        a.save()

        record=Assets.objects.get(id=1)
        self.assertEqual(record, a)

class Test_Urls(SimpleTestCase):
    def test_url_resolve_addprod(self):
        url=reverse('addprod')
        self.assertEqual(resolve(url).func, addprod)

    def test_url_resolve_purchased(self):
        url=reverse('purchased')
        self.assertEqual(resolve(url).func, purchased)

    def test_url_resolve_oldprod(self):
        url=reverse('oldprod')
        self.assertEqual(resolve(url).func, oldprod)

    def test_url_resolve_newprod(self):
        url=reverse('newprod')
        self.assertEqual(resolve(url).func, newprod)

    def test_url_resolve_check_inv(self):
        url=reverse('check_inv')
        self.assertEqual(resolve(url).func, check_inv)

    def test_url_resolve_home(self):
        url=reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_url_resolve_addsales(self):
        url=reverse('addsales')
        self.assertEqual(resolve(url).func, addsales)

    def test_url_resolve_sell(self):
        url=reverse('sell')
        self.assertEqual(resolve(url).func, sell)

    def test_url_resolve_sold(self):
        url=reverse('sold')
        self.assertEqual(resolve(url).func, sold)

    def test_url_resolve_balance(self):
        url=reverse('balance')
        self.assertEqual(resolve(url).func, balance)