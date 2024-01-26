from django.contrib import admin
from .models import CustomUserModel, AdressModel, FavoriteModel, CartModel

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(AdressModel)
admin.site.register(FavoriteModel)
admin.site.register(CartModel)