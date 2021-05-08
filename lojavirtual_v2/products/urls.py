from django.urls import path, re_path

from .views import ProductDetailView, ProductListView, ProductHomeView, SaleListView, comentario_novo

app_name = "products"

urlpatterns = [
    path("", ProductHomeView.as_view(), name="home"),
    path("list", ProductListView.as_view(), name="list"),
    path("list/<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    path("category/<slug:slug>/", ProductListView.as_view(), name="list_by_category"),
    path("sale/<slug:slug>/", SaleListView.as_view(), name="list_by_sale"),
    re_path(r'^list/(?P<pk>[0-9]+)/comentario$', comentario_novo, name="comentario_novo"),
]