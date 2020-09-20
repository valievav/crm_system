from django.urls import path
from .views import home, products, customer, create_order, update_order, delete_order

urlpatterns = [
    path('', home, name='dashboard'),
    path('products/', products, name='products'),
    path('customer/<int:pk>/', customer, name='customer'),
    path('create_order', create_order, name='create_order'),
    path('update_order/<int:pk>/', update_order, name='update_order'),
    path('delete_order/<int:pk>/', delete_order, name='delete_order'),
]
