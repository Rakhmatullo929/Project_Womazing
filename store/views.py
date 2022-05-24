from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from store import forms
from .models import *


# Create your views here.


def base_layout(request):
    return render(request, 'base_layout.html', )


def home(request):
    products = Product.objects.all()[:3]

    context = {
        'products': products
    }
    return render(request, 'home.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    product_id = request.GET.get('product')
    if product_id:
        product = Product.objects.get(pk=product_id)
        cart_item = CartItem.objects.filter(product=product)
        if not cart_item:
            cart_item = CartItem.objects.create(product=product, quantity=1)
            cart_item.save()
            return redirect('store:shop')
        for item in cart_item:
            item.quantity += 1
            item.save()
    return render(request, 'product_detail.html', {'product': product})


def contact_order(request):
    form = forms.ApplicationForms(request.POST or None)
    is_success = False
    if request.method == 'POST' and form.is_valid():
        is_success = True
        form.save()
        form = forms.ApplicationForms()
    return render(request, 'contact_order.html', {'form': form, 'is_success': is_success})


def shop(request):
    category = request.GET.get('category')
    products = Product.objects.all()
    products = products.filter(category=category) if category else products
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    return render(request, 'shop.html', {'products': products})


def about_brand(request):
    return render(request, 'about_brand.html')


def cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum([item.total_price() for item in cart_items])
    total_quantity = sum([item.quantity for item in cart_items])

    return render(request, 'cart.html',
                  {'cart_items': cart_items, 'total_quantity': total_quantity, 'total_price': total_price}
                  )


def delete_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk).delete()
    return redirect('store:cart', {'cart_item': cart_item})


def edit_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    action = request.GET.get('action')

    if action == 'take' and cart_item.quantity > 0:
        if cart_item.quantity == 1:
            cart_item.delete()
            return redirect('store:cart')
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('store:cart')
    cart_item.quantity += 1
    cart_item.save()
    return redirect('store:cart')


def create_order(request):
    cart_items = CartItem.objects.all()
    total_price = sum([item.total_price() for item in cart_items])
    amount = sum([item.quantity for item in cart_items])
    form = forms.OrderForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        order = Order.objects.create(
            name=request.POST.get('name'),
            e_mail=request.POST.get('E-mail'),
            phone=request.POST.get('phone'),
            country=request.POST.get('country'),
            city=request.POST.get('city'),
            street=request.POST.get('street'),
            house=request.POST.get('house'),
            flat=request.POST.get('flat'),
            total_price=total_price,
            customer=request.user
        )
        for cart_item in cart_items:
            OrderProduct.objects.create(
                order=order,
                product=cart_item.product,
                amount=cart_item.quantity,
                total=cart_item.total_price(),
            )

        cart_items.delete()
        return redirect('store:cart')

    form = forms.OrderForm()
    return render(request, 'order_creation_page.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'amount': amount,
        'form': form})


def order_success(request):
    form = forms.OrderForm(request.POST or None)
    is_success = False
    if request.method == 'POST' and form.is_valid():
        is_success = True
        form.save()
        form = forms.OrderForm()
    return render(request, 'order_success.html', {'form': form, 'is_success': is_success})
