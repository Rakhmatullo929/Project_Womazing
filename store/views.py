from django.db.models import Count
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from store import forms
from .forms import RateForm
from .models import *


# Create your views here.


def home(request):
    products = Product.objects.all()[:3]

    context = {
        'products': products
    }
    return render(request, 'home.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    products = Product.objects.filter()[:2]
    cart_item = CartItem.objects.filter(product=product)
    form_rating = RateForm(request.POST or None)
    if not cart_item and request.method == 'POST' and form_rating.is_valid():
        form_rating = CartItem.objects.create(
            product=product,
            quantity=1,
            size=request.POST.get('size'),
            color=request.POST.get('color'),
        )
        form_rating.save()
        return redirect('store:shop')
    for item in cart_item:
        item.quantity += 1
        item.save()
    form_rating = RateForm()
    return render(request, 'product_detail.html',
                  {'product': product, 'form_rating': form_rating, 'products': products})


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
                  {'cart_items': cart_items, 'total_quantity': total_quantity, 'total_price': total_price})


def delete_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    cart_item.delete()
    return redirect('store:cart')


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


def edit_quantity_product(request, pk):
    product_item = CartItem.objects.get(pk=pk)
    action = request.GET.get('action')

    if action == 'take' and product_item.quantity > 0:
        if product_item.quantity == 1:
            product_item.delete()
            print('+++')
            return redirect('store:product_detail')
        product_item.quantity -= 1
        print('++')
        return redirect('store:product_detail')
    print('+')
    product_item.quantity += 1
    return redirect('store:product_detail')


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
        )
        for cart_item in cart_items:
            OrderProduct.objects.create(
                order=order,
                product=cart_item.product,
                amount=cart_item.quantity,
                total=cart_item.total_price(),
            )
        return redirect('store:success')
    form = forms.OrderForm()
    return render(request, 'order_creation_page.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'amount': amount,
        'form': form})


def order_success(request):
    return render(request, 'order_success.html')


def base_layout(request):
    form = forms.FeedbackForms(request.POST or None)
    is_success = False
    if request.method == 'POST' and form.is_valid():
        is_success = True
        form.save()
        form = forms.FeedbackForms()
    return render(request, 'base_layout.html', {'form': form, 'is_success': is_success})


def get_contact(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    telephone = request.GET.get('telephone')
    Feedback.objects.create(
        client_name=name,
        client_email=email,
        client_number=telephone
    )
    return redirect('store:home')

