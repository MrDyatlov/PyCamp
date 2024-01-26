from django import template
from PRODUCTS.models import ProductsCategorieModel
from USERAPP.models import CartModel
register = template.Library()

@register.filter()
def is_numeric (value):
    try:
        value+=1
        return True
    except:
        return False

@register.simple_tag
def f_cat_list():
    categories = ProductsCategorieModel.objects.all()
    return categories

@register.simple_tag
def f_countOfBasket(request):
    total = CartModel.objects.filter(customer_id=request.user.id).count()
    return total
