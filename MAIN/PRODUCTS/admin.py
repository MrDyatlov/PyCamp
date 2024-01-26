from django.contrib import admin
from .models import ProductsModel, ProductsCategorieModel, ProductsCommentModel

# Register your models here.
admin.site.register(ProductsCategorieModel)
admin.site.register(ProductsModel)
admin.site.register(ProductsCommentModel)