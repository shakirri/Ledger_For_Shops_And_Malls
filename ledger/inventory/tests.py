from inventory.tempo import Pricing
from django.test import TestCase, Client
from django.test import SimpleTestCase
from .models import Products, Assets
from .tempo import SalesTemp, Pricing
from django.urls import reverse, resolve
from .views import addprod, purchased, oldprod, newprod, oldpurchased, check_inv, home, addsales, sell, sold, balance, inventory_calc

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

    def test_url_resolve_oldpurchased(self):
        url=reverse('oldpurchased')
        self.assertEqual(resolve(url).func, oldpurchased)

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


class Test_Views(TestCase):
    def setUp(self):
        self.client=Client()
        self.product=Products.objects.create(id="1", name="Football", amount=30, purchase_price=15, sale_price=20)
        self.product1=Products.objects.create(id="2", name="Foseball", amount=10, purchase_price=10, sale_price=20)
        self.asset=Assets.objects.create(id="1", cash=10000, profit=300, inventory_value=3000, total_purchases=1500, total_sales=2000)
        self.pricing=Pricing.objects.create(id=1, total_price=0, profit=0)


    def test_addprod(self):
        response=self.client.get(reverse('addprod'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'productexist.html')

    def test_newprod(self):
        response=self.client.get(reverse('newprod'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'addproduct.html')

    def test_oldprod(self):
        response=self.client.get(reverse('oldprod'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'oldproduct.html')

    def test_purchased(self):
        response=self.client.post(reverse('purchased'),{
            'product_id':'2',
            'name':'Bat',
            'amount':'200',
            'purchase_price':'10',
            'sale_price':'15'
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_oldpurchased(self):
        response=self.client.post(reverse('oldpurchased'),{
            'product_id':'1',
            'amount':'50',
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_check_inv(self):
        response=self.client.get(reverse('check_inv'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'productlist.html')

    def test_home(self):
        response=self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_sell(self):
        response=self.client.get(reverse('sell'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sales.html')

    def test_addsales(self):
        response=self.client.post(reverse('addsales'),{
            'product_id':'1',
            'amount':'5',
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sales.html')

    def test_sold(self):
        response=self.client.get(reverse('sold'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_balance(self):
        response=self.client.get(reverse('balance'))
        self.assertEquals(response.status_code, 200)
        
        self.assertTemplateUsed(response, 'ledger.html')

    def test_inventory(self):
        x=30*15+10*10
        self.assertEquals(inventory_calc(), x)