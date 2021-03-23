from django.urls import path

from .views import ProductDetailView, ProductListView, ProductHomeView, SaleListView

app_name = "products"

urlpatterns = [
    path("", ProductHomeView.as_view(), name="home"),
    path("list", ProductListView.as_view(), name="list"),
    path("list/<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    path("category/<slug:slug>/", ProductListView.as_view(), name="list_by_category"),
    path("sale/<slug:slug>/", SaleListView.as_view(), name="list_by_sale"),
]