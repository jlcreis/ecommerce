from django.contrib import admin
from marcador.models import Marcador
from .models import Category, Product, Images, Sale, Sale_Product, Product_Marcador


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']

class ImagesInline(admin.TabularInline):
    #list_display = ['id','product']
    model = Images

class Product_MarcadorInline(admin.TabularInline):
    model = Product_Marcador


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'category',
        'price',
        'is_available',
        'created',
        'modified'
    ]
    list_filter = ['category', 'is_available', 'created', 'modified']
    list_editable = ['price', 'is_available']
    # exclude = ['image']
    inlines = [ImagesInline]
    inlines = [Product_MarcadorInline]

    def get_images(self, obj):
        return obj.images_get


class Sale_ProductInline(admin.TabularInline):
    model = Sale_Product

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['name','slug','description','created','modified']
    inlines = [Sale_ProductInline]
