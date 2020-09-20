from django.urls import path
from .views import home, products, customer

urlpatterns = [
    path('', home, name='dashboard'),
    path('products/', products, name='products'),
    path('customer/<int:pk>/', customer, name='customer'),
]
