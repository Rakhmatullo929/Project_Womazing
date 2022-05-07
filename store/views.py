from django.shortcuts import render, redirect
from store.models import Product


# Create your views here.


def base_layout(request):
    return render(request, 'base_layout.html', )


def about(request):
    products = Product.objects.all()[:3]

    context = {
        'products': products
    }
    return render(request, 'about.html', context)


class CartItem:
    objects = None


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
    cart_item = CartItem.objects.get(pk=pk).delete()
    return redirect('store:cart')


def edit_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    action = request.GET.get('action')

    if action == 'take' and cart_item.quantity > 0:
        if cart_item.quantity == 1:
            cart_item.delete()
            return redirect('shop:cart')
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('shop:cart')
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shop:cart')


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})
