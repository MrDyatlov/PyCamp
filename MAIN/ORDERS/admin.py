from django.contrib import admin
from .models import OrderModel, OrderItemModel

# Register your models here.
admin.site.register(OrderModel)
admin.site.register(OrderItemModel)