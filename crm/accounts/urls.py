from django.urls import path
from .views import home, products, customer

urlpatterns = [
    path('', home),
    path('products/', products),
    path('customer/', customer),
]
