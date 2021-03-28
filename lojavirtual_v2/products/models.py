from autoslug import AutoSlugField #instalado de terceiros
from marcador import models as app_marcador
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel #instalado de terceiros (cria data de criação em alteração)


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)

class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name") #
    image = models.ImageField(upload_to="category/%Y/%m/%d", blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category' 
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:list_by_category", kwargs={"slug": self.slug})


class Product(TimeStampedModel):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    link_venda = models.CharField(max_length=300, null=True, blank=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})       

class Images(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)

class Sale(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    image = models.ImageField(upload_to="sales/%Y/%m/%d", blank=True)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ('name',)
        verbose_name = 'sale' 
        verbose_name_plural = 'sales'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("products:list", kwargs={"slug": self.slug})  

class Sale_Product(models.Model):
    sale = models.ForeignKey('Sale', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    objects = models.Manager()

class Product_Marcador(models.Model):
    marcador = models.ForeignKey(
        app_marcador.Marcador, related_name="product_marcadors", on_delete=models.CASCADE
    )
    product = models.ForeignKey('Product', on_delete=models.CASCADE)