from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    image = models.FileField(null=True)

    def __str__(self):
        return f'{self.title}, {self.price}'


class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    def total_price(self):
        return self.product.price * self.quantity


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'store_categories'


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'store_types'


class Application(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    number = models.CharField(max_length=20)
    message = models.TextField(max_length=255)

    def __str__(self):
        return F'{self.name} {self.email} {self.number} {self.message}'

