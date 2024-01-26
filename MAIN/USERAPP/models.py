from django.db import models
from django.contrib.auth.models import AbstractUser
from PRODUCTS.models import ProductsModel

# Create your models here.
class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to="users/", blank=True, null=True, verbose_name="Avatar")
    phoneNumber = models.CharField(verbose_name="Phone Number", max_length=10, blank=True, null=True)

    class Meta:
        db_table = "auth_user"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class AdressModel(models.Model):
    customer = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, verbose_name="Customer", related_name="adress")
    adress_title = models.CharField(verbose_name="Adress Title", max_length=50, null=False, blank=False)
    adress_city = models.CharField(verbose_name="City", max_length=50)
    adress_district = models.CharField(verbose_name="District", max_length=50)
    adress_neighborhood = models.CharField(verbose_name="Neighborhood", max_length=50)
    adress_description = models.TextField(verbose_name="Adress Detials", max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.adress_title

    class Meta:
        db_table = "Adress"
        verbose_name_plural = "Adresses"


class FavoriteModel(models.Model):
    customer = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, verbose_name="Customer")
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE, verbose_name="Product")

    def __str__(self):
        return str(self.product)

    class Meta:
        db_table = "Favorites"
        verbose_name_plural = "Favorities"


class CartModel(models.Model):
    customer = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, verbose_name="Customer")
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE, verbose_name="Product")
    amount = models.IntegerField(verbose_name="Amount", null=False)


    def __str__(self):
        return str(self.product)


    class Meta:
        db_table = 'Cart'
        verbose_name_plural = "Basket"