from django.urls import path
from . import views

app_name = "USERAPP"

urlpatterns = [
    path("profile/", views.profile_view, name="profile"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("basket/", views.cart_view, name="cart"),
    path("checkout/", views.chechkout_view, name="checkout"),
    path("favorites/", views.favorites_view, name="favorites"),
    path("update_item/", views.update_item_view, name="update_item"),
    path("update-cart/", views.update_cart_view, name="update-cart"),
    path("update-favorites/", views.update_favorites, name="update-favorites"),
    path("orders", views.orders_view, name="orders")
]