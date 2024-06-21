from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category_products/<int:id>/', views.category_products, name='category_products'),
    path('product/<slug:slug>/', views.single_product, name='single_product'),
    path('search/', views.search, name='search'),
]
