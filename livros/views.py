from django.http import JsonResponse
from .models import Livro


def listar_livros(request):
    livros = Livro.objects.select_related('autor', 'categoria').all().order_by('id')

    dados = [
        {
            'id': livro.id,
            'titulo': livro.titulo,
            'isbn': livro.isbn,
            'ano_publicacao': livro.ano_publicacao,
            'disponivel': livro.disponivel,
            'autor': {
                'id': livro.autor.id,
                'nome': livro.autor.nome,
            },
            'categoria': {
                'id': livro.categoria.id,
                'nome': livro.categoria.nome,
            },
        }
        for livro in livros
    ]

    return JsonResponse(dados, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
