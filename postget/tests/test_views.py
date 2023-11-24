from django.test import TestCase, Client
from django.urls import reverse
from postget.models import Customer, Food, Order, Tag
class TestViews(TestCase):

    def __int__(self):
        self.client = Client()


    def test_orders(self):
        url = self.client.get(reverse('orders'))

        self.assertEquals(url.status_code, 200)
        self.assertTemplateUsed(url, 'orders.html')
    

    def test_customers(self):
        Customer.objects.create(name='Kofi', email='kofi@gmail.com')
        url = self.client.get(reverse('customers', args=['Kofi']))

        self.assertEquals(url.status_code, 200)
        self.assertTemplateUsed(url, 'customers.html')
    

    def test_foods(self):
        url = self.client.get(reverse('foods'))

        self.assertEquals(url.status_code, 200)
        self.assertTemplateUsed(url, 'foods.html')
    
    
    def test_create_order_get(self):
        customer1 = Customer.objects.create(name='Kofi', email='kofi@gmail.com')
        url = self.client.get(reverse('create_order', args=[customer1]))

        self.assertEquals(url.status_code, 200)
        self.assertTemplateUsed(url, 'place_order.html')


    def test_create_order_post(self):
        customer1 = Customer.objects.create(name='Kofi', email='kofi@gmail.com')
        tag1 = Tag.objects.create(tag='Invoice1')

        food1 = Food.objects.create(
            name='Fufu',
            price=100,
            description='Tasty',
            date_created='',
        )
        food1.tag.set([tag1])

        order1 = Order.objects.create(
            customer_name=customer1,
            food=food1,
            location='Bantama',
            delivery='Pick Up'
        )
        
        url = self.client.post(reverse('create_order', args=[customer1]))
        self.assertEquals(url.status_code, 200)


    def test_api(self):
        url = self.client.get(reverse('api'))

        self.assertEquals(url.status_code, 200)
        