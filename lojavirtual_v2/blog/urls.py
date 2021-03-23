from django.urls import path, re_path, include
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.BlogIndex.as_view(), name='index'),
    path('posts', views.PostList.as_view(), name='lista_post'),
    re_path(r'^post/(?P<pk>[0-9]+)$', views.BlogDetail.as_view(), name='post'),
    re_path(r'^post/(?P<pk>[0-9]+)/comentario$', views.comentario_novo, name="comentario_novo"),
    re_path(r'^comentario/(?P<pk>[0-9]+)/like$', views.comentario_like, name="comentario_like"),
    re_path(r'^comentario/(?P<pk>[0-9]+)/unlike$', views.comentario_unlike, name="comentario_unlike"),
]