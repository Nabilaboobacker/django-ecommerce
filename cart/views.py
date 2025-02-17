from django.shortcuts import render, get_object_or_404, redirect
from . models import Cart, CartItem
from shop.models import Product

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def cart(request, grand_total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            grand_total += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity
    except Cart.DoesNotExist:
        pass
    context = {'grand_total':grand_total,
               'quantity':quantity,
               'cart_items':cart_items
               } 
    return render(request, 'cart/cart.html', context)




def add_cart(request, id):
    product = get_object_or_404(Product, pk=id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id= _cart_id(request))
        cart.save()
    
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save() 
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(cart=cart, product=product, quantity=1)
        cart_item.save
    print(cart_item.product.product)
    return redirect('cart')


def remove_cart(request, id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=id)
    cart_item = CartItem.objects.get(cart=cart, product=product)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')


def delete_cart_item(request, id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    return redirect('cart')