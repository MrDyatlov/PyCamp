from django.db import models
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from unidecode import unidecode

# Create your models here.
class ProductsCategorieModel(models.Model):
    categorie_title = models.CharField(verbose_name="Categorie Name", max_length=50)
    material_icon = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.categorie_title

    class Meta:
        db_table = "Product_Categorie"
        verbose_name_plural = "Categories"


class ProductsModel(models.Model):
    class Meta:
        db_table = "Products"
        verbose_name_plural = "Productses"

    product_title = models.CharField(verbose_name="Product Name", max_length=50)
    product_price = models.FloatField(verbose_name="Product Price")
    product_description = models.TextField(verbose_name="Product Description", max_length=500)
    product_image = models.ImageField(verbose_name="Product Image", upload_to="media/", blank=True, null=True)
    product_shipping = models.BooleanField(verbose_name="Free Cargo?", default=False, null=True, blank=True)
    product_categorie = models.ManyToManyField(ProductsCategorieModel, verbose_name="Categorie")
    slug = AutoSlugField(populate_from="product_title", unique=True, blank=True, default="", editable=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        title = self.product_title
        self.slug=slugify(unidecode(title))
        super(ProductsModel, self).save()

    def __str__(self):
        return self.product_title


class ProductsCommentModel(models.Model):
    customer = models.ForeignKey("USERAPP.CustomUserModel", verbose_name="Customer", on_delete=models.CASCADE, default="")
    comment_date = models.DateTimeField(auto_now_add=True, verbose_name="Comment Date")
    product = models.ForeignKey(ProductsModel, verbose_name="Product Name", on_delete=models.CASCADE, related_name="comments")
    comment_text = models.TextField(max_length=500, verbose_name="Comment", default=None)

    def __str__(self):
        return self.comment_text

    class Meta:
        db_table = "Comments"
        verbose_name_plural = "Product Comments"