from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.FileField(null=True)
    category = models.ForeignKey('store.Category', default=None, on_delete=models.CASCADE)
    type = models.ForeignKey('store.Type', default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.price}'

    class Meta:
        db_table = 'store_products'


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
    name = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    number = models.CharField(max_length=20, null=True)
    message = models.TextField(max_length=255, null=True)

    def __str__(self):
        return F'{self.name} {self.email} {self.number} {self.message}'


COLOR_CHOICES = [
    (1, 'BROWN'),
    (2, 'GREY'),
    (3, 'RED'),
    (4, 'YELLOW'),
]

SIZE_CHOICES = [
    ('s', 'S'),
    ('m', 'M'),
    ('l', 'L'),
    ('xl', 'XL'),
    ('xll', 'XLL'),
]


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    size = models.CharField(choices=SIZE_CHOICES, max_length=3, null=True)
    color = models.PositiveSmallIntegerField(choices=COLOR_CHOICES, null=True)

    def __str__(self):
        return self.product.title

    def total_price(self):
        return self.product.price * self.quantity


class Order(models.Model):
    name = models.CharField(max_length=255, null=True)
    e_mail = models.EmailField(null=True)
    phone = models.CharField(max_length=13, null=True)
    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    street = models.CharField(max_length=50, null=True)
    house = models.CharField(max_length=50, null=True)
    flat = models.CharField(max_length=50, null=True)
    total_price = models.IntegerField()

    def __str__(self):
        return 'Order # %s' % (str(self.id))


class OrderProduct(models.Model):
    order = models.ForeignKey('store.Order', on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    amount = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return '%s x%s - %s' % (self.product, self.amount, self.order)


class Feedback(models.Model):
    client_name = models.CharField(max_length=30, null=True)
    client_email = models.EmailField(null=True)
    client_number = models.CharField(max_length=30, null=True)

# class Review(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.product
