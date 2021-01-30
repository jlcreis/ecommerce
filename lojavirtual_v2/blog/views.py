from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Post, Comentario
from .forms import ComentarioForm

# Create your views here.
#def BlogIndex (request):
#    return render (request, 'home.html')
class BlogIndex (ListView):
    paginate_by = 3

    def get_queryset(self):
        queryset = Post.objects.all()
        print ("blog passou")
        return queryset

class BlogDetail (DetailView):
    model = Post
    

def comentario_novo (request, pk):
    post = get_object_or_404 (Post, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm (request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect (reverse ('blog:post', kwargs={'pk': post.pk}))
    else:
        form = ComentarioForm()
    return render (request, 'blog/comentario.html', {'form': form})

def comentario_like(request, pk):
    comentario = get_object_or_404 (Comentario, pk=pk)
    comentario.like()
    comentario.save()
    return redirect (reverse ('blog:post', kwargs={'pk': comentario.post_id}))

def comentario_unlike(request, pk):
    comentario = get_object_or_404 (Comentario, pk=pk)
    comentario.unlike()
    comentario.save()
    return redirect (reverse ('blog:post', kwargs={'pk': comentario.post_id}))
