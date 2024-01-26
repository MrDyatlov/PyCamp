from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ProductsModel, ProductsCategorieModel, ProductsCommentModel
from django.core.paginator import Paginator
from .forms import CommentForm

# Create your views here.
def categorie_products_view(request, cat_title):
    categories = ProductsCategorieModel.objects.get(categorie_title=cat_title)
    products = ProductsModel.objects.filter(product_categorie=categories.id)
    return render(request, "PRODUCTS/products.html", context={"products": products, "categories": categories})


def products_view(request):
    keyword = request.GET.get("keyword")
    page = request.GET.get("page")
    if keyword:
        products = ProductsModel.objects.filter(product_title__contains=keyword)
    else:
        products = ProductsModel.objects.all()
        pagination = Paginator(products, 3)

    return render(request, "PRODUCTS/products.html", context={"products": pagination.get_page(page)})


def product_detail_view(request, slug):
    try:
        product = ProductsModel.objects.get(slug=slug)
    except:
        return redirect("404.html")
    try:
        comments = ProductsCommentModel.objects.filter(product=product).order_by("-comment_date")
    except:
        comments = None

    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.customer = request.user
        comment.comment_text = comment_form.cleaned_data.get("comment_text")
        comment.product = product
        comment.save()
        return redirect(reverse("product-details", slug=slug))
    return render(request, "PRODUCTS/product-details.html", context={"form": comment_form, "comments": comments})