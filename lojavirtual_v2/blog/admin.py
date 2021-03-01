from django.contrib import admin

from . import models


class PostAdmin (admin.ModelAdmin):
    list_display = ('titulo', 'publicado', 'autor', 'data_criado')
    fields = ('titulo', 'publicado', 'image', 'texto', 'link_media')
    list_filter = ('autor',)
    
    def save_model(self, request, obj, form, change):
        obj.autor = request.user 
        obj.save ()
        
# Register your models here.
admin.site.register (models.Post, PostAdmin)
admin.site.register (models.Comentario)