from django.contrib import admin
from .models import Livro


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'categoria', 'ano_publicacao', 'disponivel')
    list_filter = ('disponivel', 'categoria')
    search_fields = ('titulo', 'isbn', 'autor__nome')
