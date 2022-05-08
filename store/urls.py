from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.about, name='main'),
    path('cart/', views.cart, name='cart'),
    path('delete_cart_item/<int:pk>', views.delete_cart_item, name='delete_cart_item'),
    path('edit_cart_item/<int:pk>', views.edit_cart_item, name='edit_cart_item'),
    path('product/<int:pk>', views.product_detail, name='product_detail'),
    path('contact/', views.order_registration, name='order_registration'),

]
