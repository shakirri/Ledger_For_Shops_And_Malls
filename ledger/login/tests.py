from django.http import response
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

class Test_Views(TestCase):
    def setUp(self):
        self.client=Client()
        self.users=Users.objects.create(userid="Pele", passw="Brazil")

    def test_login(self):
        response=self.client.get(reverse('login1'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_checkpass(self):
        response=self.client.post(reverse('checkpass'), {
            'username':'Pele',
            'password':'Brazil'
        })
        response1=self.client.post(reverse('checkpass'), {
            'username':'Maradona',
            'password':'Brazil'
        })
        response2=self.client.post(reverse('checkpass'), {
            'username':'Pele',
            'password':'Argentina'
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response1, 'error.html')
        self.assertTemplateUsed(response2, 'error.html')