from django.db import models
from autores.models import Autor
from categorias.models import Categoria


class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13, unique=True)
    ano_publicacao = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    # Um autor pode escrever vários livros, enquanto cada livro possui um autor principal.
    # Por isso, a relação Autor -> Livro é 1:N e a ForeignKey fica no model Livro.
 
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name='livros')

   # Uma categoria pode agrupar vários livros e cada livro pertence a uma categoria.
    # Essa segunda relação também é 1:N e ajuda a organizar o acervo da biblioteca.
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='livros')

    def __str__(self):
        return self.titulo
