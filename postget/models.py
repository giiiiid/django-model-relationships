from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)


class Tag(models.Model):
    tag = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.tag)


class Food(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.name)
    
    # def save(self, *args, **kwargs):
    #     self.description = f'Contains {self.tag}'
    #     super(Food, self).save(*args, **kwargs)

class Order(models.Model):
    locs = (
        ('Bantama', 'Bantama'),
        ('Santasi', 'Santasi'),
        ('Abrepo', 'Abrepo'),
        ('North', 'North'),
        ('South', 'South'),
        )
    
    category = (
        ('Pick up', 'Pick up'),
        ('Delivery', 'Delivery')
        )
    customer_name = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    food = models.ForeignKey(Food, null=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=150, null=True, choices=locs)
    invoice = models.CharField(max_length=150, null=True)
    delivery = models.CharField(max_length=150, null=True, choices=category)

    def __str__(self):
        return str(self.invoice)
    
    # def save(self, *args, **kwargs):
    #     self.invoice = 
    
    