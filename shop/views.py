from django.shortcuts import render, get_object_or_404
from . models import Product, Category
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.views import _cart_id
from cart.models import Cart, CartItem

# Create your views here.
def home(request):
    new_products = Product.objects.filter(is_new_arrival=True)
    paginator = Paginator(new_products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'new_products':page_obj,}
    return render(request, 'home.html', context)

def category_products(request, id):
    products = Product.objects.filter(product_category=id)
    category = get_object_or_404(Category, pk=id)
    context = {'products':products,
               'category':category,}
    return render(request, 'category_products.html', context)


def single_product(request, slug):
    product = get_object_or_404(Product, product_slug=slug)
    
    in_cart = False  # Initialize in_cart to False
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        in_cart = CartItem.objects.filter(cart=cart, product=product).exists()
    except Cart.DoesNotExist:
        cart = None  # Cart does not exist, so in_cart remains False
    
    context = {
        'product': product,
        'in_cart': in_cart,
    }
    
    return render(request, 'single_product.html', context)

def search(request):
    context={}
    if request.method == 'POST':
        search_key = request.POST['search_key']
        products = Product.objects.filter(Q(product__icontains=search_key)|Q(product_description__icontains=search_key))
        context = {'products':products,
               'search_key':search_key,}
    return render(request, 'search.html', context)  