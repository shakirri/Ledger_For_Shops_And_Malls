from django.test import TestCase, Client
from django.test import SimpleTestCase
from .models import Users
from django.urls import reverse, resolve
from .views import login1, checkpass

# Create your tests here.

class Test_Models(TestCase):
    
    def test_fields(self):
        users=Users()
        users.userid="Ronaldo"
        users.passw="ManU"
        users.save()

        record=Users.objects.get(pk=1)
        self.assertEqual(record, users)

class Test_Urls(SimpleTestCase):
    def test_url_resolve_login(self):
        url=reverse('login1')
        #print(url)
        self.assertEqual(resolve(url).func, login1)

    def test_url_resolve_check(self):
        url=reverse('checkpass')
        self.assertEqual(resolve(url).func, checkpass)
