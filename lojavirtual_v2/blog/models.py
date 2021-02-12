from django.db import models
from django.conf import settings

# Create your models here.
class Post (models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    publicado = models.BooleanField(default=False)
    data_criado = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)
    link_media = models.CharField(max_length=300, null=True)

    def __str__ (self):
        return self.titulo

class Comentario (models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    likes = models.IntegerField(default=0)
    unlikes = models.IntegerField(default=0)
    data_criado = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.autor + " - " + str (id)

    def like (self):
        self.likes += 1

    def unlike (self):
        self.unlikes += 1

    