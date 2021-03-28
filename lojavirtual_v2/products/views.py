#from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django.shortcuts import render

from .models import Category, Product, Images, Sale, Sale_Product


class ProductDetailView(DetailView):
    
    #extra_context = {"form": CartAddProductForm()}
    def get_queryset(self):
        queryset = Product.available.all()
        return queryset

class ProductHomeView(TemplateView):
    template_name = "products/product_home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['promocao_list'] = Sale.available.all()
        context['product_list'] = Product.available.all()[:4]
        context["categories"] = Category.objects.all()
        return context

class ProductListView(ListView):
    category = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Product.available.all()
        category_slug = self.kwargs.get("slug")
        print(category_slug)
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Category.objects.all()
        return context

class SaleListView(TemplateView):
    template_name = "products/sale_product_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Sale_Product.objects.all()
        sale_slug = self.kwargs.get("slug")
        if sale_slug:
            print(sale_slug)
            self.sale = get_object_or_404(Sale, slug=sale_slug)
            print(self.sale.id)
            queryset = queryset.filter(sale=self.sale.id)
        context['sale_list'] = queryset
        context["categories"] = Category.objects.all()
        return context
    """
    def get_queryset(self):
        queryset = Sale_Product.objects.all()
        sale_slug = self.kwargs.get("slug")
        if sale_slug:
            print(sale_slug)
            self.sale = get_object_or_404(Sale, slug=sale_slug)
            print(self.sale.id)
            queryset = queryset.filter(sale=self.sale.id)
        return queryset

        self.sale_product = get_object_or_404(Sale_Product, sale=self.sale.id)
        """