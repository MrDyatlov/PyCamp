from django.urls import path
from . import views

app_name = "PRODUCTS"

urlpatterns = [
    path("categorie/<str:cat_title>", views.categorie_products_view, name="product-categories"),
    path("", views.products_view, name="products"),
    path("product/<slug:slug>", views.product_detail_view, name="product-details")
]