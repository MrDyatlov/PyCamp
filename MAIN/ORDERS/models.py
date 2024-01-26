import random

from django.db import models
from USERAPP.models import CustomUserModel, AdressModel
from PRODUCTS.models import ProductsModel
from autoslug import AutoSlugField
import unidecode
from django.template.defaultfilters import slugify
import random, string

# Create your models here.
class OrderModel(models.Model):
    customer = models.ForeignKey(CustomUserModel, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Customer")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Order Date")
    complete = models.BooleanField(verbose_name="Completed?", default=False, null=True, blank=False)
    order_adress = models.ForeignKey(AdressModel, null=True, blank=False, on_delete=models.SET_NULL, verbose_name="Order Adress")
    transaction_id = models.CharField(max_length=200, null=True, verbose_name="Transaction Number")
    slug = models.SlugField(null=True, unique=True, editable=True)


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.id is None:
            title = self.customer.username + "-"
            title = slugify(unidecode(title))
            self.slug = slugify(unidecode(title)) + "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(20))
        super(OrderModel, self).save()


    def __str__(self):
        return f"{self.id} {self.customer.username}"

    class Meta:
        db_table = "Orders"
        verbose_name_plural = "Orderses"


class OrderItemModel(models.Model):
    product = models.ForeignKey(ProductsModel, on_delete=models.SET_NULL, null=True, verbose_name="Product")
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, null=True, verbose_name="Order")
    quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name="Quantitiy")

    def __str__(self):
        return f"{self.product}"

    class Meta:
        db_table = "Order_Items"
        verbose_name_plural = "Order Products"