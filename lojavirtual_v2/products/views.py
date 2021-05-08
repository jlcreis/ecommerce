#from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView
from django.shortcuts import render
from .forms import ComentarioForm

from .models import Category, Product, Images, Sale, Sale_Product, Comentario


class ProductDetailView(DetailView):
    category = None
    #extra_context = {"form": CartAddProductForm()}
    def get_queryset(self):
        queryset = Product.available.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Category.objects.all()
        context['product_list_novidade'] = Product.available.all()[:5]
        context['comentarios'] = Comentario.available.all()
        return context


class ProductHomeView(TemplateView):
    template_name = "products/product_home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['promocao_list'] = Sale.available.all()
        context['product_list_novidade'] = Product.available.all()[:4]
        context['product_list_preco'] = Product.available.all()[:4]
        context['product_list_categoria'] = Product.available.all()[:2]
        context["categories"] = Category.objects.all()
        return context

class ProductListView(ListView):
    category = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Product.available.all()
        category_slug = self.kwargs.get("slug")
        busca = self.request.GET.get("procurar")

        print(category_slug)
        print(busca)

        if busca:
            queryset = queryset.filter(name__icontains = busca)

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

def comentario_novo (request, pk):
    product = get_object_or_404 (Product, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm (request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.product = product
            comentario.save()
            return redirect (reverse ('products:detail', kwargs={'slug': product.slug}))
    else:
        form = ComentarioForm()
    return render (request, 'products/comentario.html', {'form': form})