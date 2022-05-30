from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('product/<int:pk>', views.product_detail, name='product_detail'),
    path('contact/', views.contact_order, name='contact_order'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about_brand, name='about_brand'),
    path('cart/', views.cart, name='cart'),
    path('delete_cart_item/<int:pk>', views.delete_cart_item, name='delete_cart_item'),
    path('edit_cart_item/<int:pk>', views.edit_cart_item, name='edit_cart_item'),
    path('edit_quantity_product/<pk>', views.edit_quantity_product, name='edit_quantity_product'),
    path('cart/create_order', views.create_order, name='create_order'),
    path('create_oder/success', views.order_success, name='success'),
    path('get_contact/', views.get_contact, name='get_contact_url')
]
