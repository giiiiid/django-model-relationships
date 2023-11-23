from django.test import SimpleTestCase
from django.urls import reverse, resolve
from postget.views import orders, customers, foods, create_order, api

# from django.test import SimpleTestCase
# from django.urls import reverse, resolve
# from ..views import index, user_home, detail, update, done, delete, search, sign_up, login_user, logout_user, crudApi

class TestUrls(SimpleTestCase):

    def test_orders(self):
        url = reverse('orders')

        self.assertEquals(resolve(url).func, orders)
    

    def test_customers(self):
        url = reverse('customers', args=['name'])

        self.assertEquals(resolve(url).func, customers)
    

    def test_foods(self):
        url = reverse('foods')

        self.assertEquals(resolve(url).func, foods)
    

    def test_create_order(self):
        url = reverse('create_order', args=['name'])

        self.assertEquals(resolve(url).func, create_order)
    

    def test_api(self):
        url = reverse('api')

        self.assertEquals(resolve(url).func, api)