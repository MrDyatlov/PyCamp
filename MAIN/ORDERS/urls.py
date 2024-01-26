from django.urls import path
from . import views

app_name = "ORDERS"

urlpatterns = [
    path("", views.payment_view, name="payment")
]