from django.contrib import admin
from .models import Marcador

# Register your models here.

@admin.register(Marcador)
class MarcadorAdimin(admin.ModelAdmin):
    list_display = ['nome']
