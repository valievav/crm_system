from django.db.models import Count
from django.shortcuts import render, redirect

from .models import Customer, Product, Order
from .forms import OrderForm


def home(request):
    orders = Order.objects.all()
    orders_per_customer_raw = orders.values('customer',
                                            'customer__first_name',
                                            'customer__last_name').annotate(total=Count('customer__first_name'))
    orders_per_customer = [(order['customer'],
                            f"{order['customer__first_name']} {order['customer__last_name']}",
                            order['total'])
                           for order in orders_per_customer_raw]

    total_orders = orders.count()
    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'orders_per_customer': orders_per_customer,
        'total_orders': total_orders,
        'orders_delivered': orders_delivered,
        'orders_pending': orders_pending
    }
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'accounts/products.html', context)


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count

    context = {
        'customer': customer,
        'orders': orders,
        'orders_count': orders_count
    }
    return render(request, 'accounts/customer.html', context)


def create_order(request):
    form = OrderForm()

    # get user-entered data from POST request
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'accounts/order_form.html', context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'accounts/order_form.html', context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {
        'order': order
    }
    return render(request, 'accounts/order_delete.html', context)
