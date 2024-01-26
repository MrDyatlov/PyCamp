from django.shortcuts import render,redirect
from django.urls import reverse
from USERAPP.models import CartModel
from .models import OrderItemModel, OrderModel


def payment_view(request):
    order_items = CartModel.objects.filter(customer_id=request.user.id)
    if not order_items:
        return redirect(reverse("PRODUCTS:products"))
    ORDER = OrderModel.objects.create(customer_id=request.user.id, complete=False)
    ORDER.save()
    for item in order_items:
        ITEM=OrderItemModel.objects.create(product_id=item.product.id, quantity=item.amount, order_id=ORDER.id)
        ITEM.save()
    order_items.delete()

    return render(request,"ORDERS/success.html")
