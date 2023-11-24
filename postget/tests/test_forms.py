from django.test import TestCase
from postget.forms import OrderForms
from postget.models import Customer, Tag, Food, Order


class TestForms(TestCase):
    def test_forms(self):
        new_cus = Customer.objects.create(name='Kofi', email='kofi@gmail.com')
        tag1 = Tag.objects.create(tag='Chicken')
        food1 = Food.objects.create(
            name='Fufu',
            price=100,
            description='Tasty',
            date_created='',
        )
        food1.tag.set([tag1])

        forms = OrderForms(data={
            'customer_name':new_cus,
            'food':food1,
            'location':'Bantama',
            'invoice':'Invoice1',
            'delivery':'Pick Up'
        })
        self.assertFalse(forms.is_valid())
    
    
    def test_forms_no_data(self):
        forms = OrderForms(data={})
        self.assertEquals(len(forms.errors), 5)
