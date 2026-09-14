from django.db import models
from autores.models import Autor
from categorias.models import Categoria


class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13, unique=True)
    ano_publicacao = models.IntegerField()
    disponivel = models.BooleanField(default=True)

 
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name='livros')

   
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='livros')

    def __str__(self):
        return self.titulo
