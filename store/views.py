from django.shortcuts import render, redirect
from store import forms
from store.models import Product, CartItem


# Create your views here.


def base_layout(request):
    return render(request, 'base_layout.html', )


def home(request):
    products = Product.objects.all()[:3]

    context = {
        'products': products
    }
    return render(request, 'home.html', context)


def products_list(request):
    product_id = request.GET.get('product')
    category = request.GET.get('category')
    type = request.GET.get('type')
    products = Product.objects.all()
    if product_id:
        product = Product.objects.get(pk=product_id)
        cart_item = CartItem.objects.filter(product=product)
        if not cart_item:
            cart_item = CartItem.objects.create(customer=request.user, product=product, quantity=1)
            cart_item.save()
            return redirect('store:products')
        for item in cart_item:
            item.quantity += 1
            item.save()
    products = products.filter(category=category) if category else products
    products = products.filter(type=type) if type else products
    return render(request, 'home.html', {'products': products})


def cart(request):
    cart_items = CartItem.objects.filter(customer=request.user)
    total_price = sum([item.total_price() for item in cart_items])
    total_quantity = sum([item.quantity for item in cart_items])

    return render(
        request,
        'cart.html',
        {'cart_items': cart_items, 'total_quantity': total_quantity, 'total_price': total_price}
    )


def delete_cart_item(request, pk):
    cart_item = CartItem.objects.filter(pk=pk)
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


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
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
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})


def about_brand(request):
    return render(request, 'about_brand.html')
