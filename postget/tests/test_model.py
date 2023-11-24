from django.test import TestCase
from postget.models import Customer, Tag, Food, Order
class TestModel(TestCase):

    def test_customer_creation(self):
        new_cus = Customer.objects.create(name='Kofi', email='kofi@gmail.com')
        self.assertEquals(new_cus.name, 'Kofi')
    
    def test_tag(self):
        tag1 = Tag.objects.create(tag='Chicken')
        self.assertEquals(tag1.tag, 'Chicken')
    
    def test_food(self):
        tag1 = Tag.objects.create(tag='Chicken')
        food1 = Food.objects.create(
            name='Fufu',
            price=100,
            description='Tasty',
            date_created='',
        )
        food1.tag.set([tag1]) # or food1.tag.add(tag1)

        # self.assertEquals(food1.tag, tag1)   # AssertionError

    
    def test_order(self):
        new_cus = Customer.objects.create(name='Kofi', email='kofi@gmail.com')
        tag1 = Tag.objects.create(tag='Chicken')
        food1 = Food.objects.create(
            name='Fufu',
            price=100,
            description='Tasty',
            date_created='',
        )
        food1.tag.set([tag1])

        order1 = Order.objects.create(
            customer_name=new_cus,
            food=food1,
            location='Bantama',
            invoice='Invoice1',
            delivery='Pick Up'
        )

        self.assertEquals(order1.invoice, 'Invoice1')
        self.assertEquals(order1.customer_name, new_cus)
        self.assertEquals(order1.food, food1)
        # self.assertEquals(order1.food.tag, tag)  # ManyToManyField error