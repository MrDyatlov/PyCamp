from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import CustomUserModel, FavoriteModel, CartModel, AdressModel
from .forms import LoginForm, RegisterForm, AdressForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ORDERS.forms import OrderForm
from ORDERS.models import OrderModel
import json
from PRODUCTS.models import ProductsModel
from django.http import JsonResponse


# Create your views here.
def anyUsername(new_username):
    customer_username = CustomUserModel.objects.filter(username=new_username)
    if not customer_username:
        return True
    else:
        return False


def anyMail(new_mail):
    customer_mail = CustomUserModel.objects.filter(email=new_mail)
    if not customer_mail:
        return True
    else:
        return False


def register_view(request):
    if request.user.is_authenticated:
        return redirect(reverse("PRODUCTS:products"))
    else:
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            if anyUsername(username)==False:
                messages.error(request, "This username is already taken.")
                return redirect(reverse("USERAPP:register"))
            if anyMail(email)==False:
                messages.error(request, "This email is already in use.")
                return redirect(reverse("USERAPP:register"))

            new_user = User(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            login(request, new_user)
            messages.success(request, "You have successfully registered.")
            return redirect(reverse("PRODUCTS:products"))

        return render(request, "USERAPP/register.html", context={"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse("PRODUCTS:products"))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse("PRODUCTS:products"))
            else:
                messages.error(request, "You have made an incorrect entry. Please check again and try again.")
                return render(request, "USERAPP/login.html", context={"form": form})

        return render(request, "USERAPP/login.html", context={"form": form})




@login_required(login_url="USERAPP:login")
def logout_view(request):
    logout(request)
    return redirect(reverse("PRODUCTS:products"))


@login_required(login_url="USERAPP:login")
def cart_view(request):
    products = CartModel.objects.filter(customer=request.user)
    total = 0
    for product in products:
        total += product.amount * product.product.product_price
    return render(request, "USERAPP/cart.html", context={"products": products, "total": total})


def chechkout_view(request):
    cart_items = CartModel.objects.filter(customer_id=request.user.id)

    if not cart_items:
        return redirect(reverse("PRODUCTS:products"))
    else:
        form = OrderForm(request.POST or None)
        if form.is_valid():
            adress = form.save(commit=False)
            adress.adress_title = form.cleaned_data.get("adress_title")
            adress.customer = request.user
            adress.save()
            messages.success(request, "Adress Successfully Added")
            return redirect(reverse("checkout"))
        customer_adress = AdressModel.objects.filter(customer=request.user)
        products = CartModel.objects.filter(customer=request.user)
        total = 0

        for product_ in products:
            total += product_.product.product_price * product_.amount

        return render(request, "USERAPP/checkout.html", context={"products": products, "total": total, "form": form, "customer_adress": customer_adress})


def favorites_view(request):
    favorites = FavoriteModel.objects.filter(customer=request.user)
    return render(request, "USERAPP/favorites.html", context={"favorites": favorites})

def update_item_view(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data["action"]
    _customer = request.user

    product = ProductsModel.objects.get(id=productId)
    cartItem = CartModel.objects.filter(customer=_customer).filter(product_id=productId)
    if not cartItem:
        cartItem = CartModel.objects.create(product_id=productId, customer=_customer, amount=1)
        cartItem.save()
    else:
        cartItem = CartModel.objects.get(customer=_customer, product_id=productId)
        if action == "add":
            cartItem.amount += 1
        elif action == "remove":
            cartItem.amount -= 1
        cartItem.save()
    return JsonResponse(
        "<div class='alert alert-success m-3 p-3 rounded'><i class='fa fa-check' aria-hidden='true'></i> Product has been successfully added to your cart.</div>",
        safe=False)


def update_cart_view(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data["action"]
    cartItem = CartModel.objects.get(product_id=productId, customer_id=request.user.id)
    if action == "add":
        cartItem.amount += 1
        cartItem.save()
        messages.success(request, "Your cart has been successfully updated.")
    elif action == "remove":
        if cartItem.amount == 1:
            cartItem.delete()
            messages.success(request, "Product has been successfully removed from your basket.")
        else:
            cartItem.amount -= 1
            cartItem.save()
            messages.success(request, "Your basket has been successfully updated.")

    return JsonResponse("asdf", safe=False)


def update_favorites(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data["action"]
    if action == "add":
        try:
            favItem = FavoriteModel.objects.get(customer_id=request.user.id, product_id=productId)
            return JsonResponse(
                "<div class='alert alert-danger m-3 p-3 rounded'><i class='fa fa-check' aria-hidden='true'></i> The product is already in your favorites.</div>",
                safe=False)
        except:
            newFavItem = FavoriteModel.objects.create(customer_id=request.user.id, product_id=productId)
            newFavItem.save()
            return JsonResponse(
                "<div class='alert alert-success m-3 p-3 rounded'><i class='fa fa-check' aria-hidden='true'></i> The product has been successfully added to your favorites.</div>",
                safe=False)

    elif action == "remove":
        favItem = FavoriteModel.objects.get(customer_id=request.user.id, product_id=productId)
        favItem.delete()

    return JsonResponse(
        "<div class='alert alert-success m-3 p-3 rounded'><i class='fa fa-check' aria-hidden='true'></i> The product has been successfully removed from your Favorites.</div>",
        safe=False)


def orders_view(request):
    customerOrders = OrderModel.objects.filter(customer_id=request.user.id)

    return render(request, "ORDERS/orders.html", {"customerOrderList": customerOrders})


@login_required(login_url="USERAPP:login")
def profile_view(request):
    user = CustomUserModel.objects.filter(id=request.user.id)
    user_adress = AdressModel.objects.filter(customer=request.user)
    adress_form = AdressForm(request.POST)
    if adress_form.is_valid():
        adress = adress_form.save(commit=False)
        adress.customer = request.user
        adress.save()
        messages.success(request, "Adress Successfully Added")
        return redirect(reverse("USERAPP:profile"))
    return render(request, "USERAPP/profile.html", context={"user": user[0], "userAddress": user_adress, "adresForm": adress_form})