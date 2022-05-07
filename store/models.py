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
