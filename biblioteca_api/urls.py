from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def inicio(request):
    return JsonResponse({
        'projeto': 'API Biblioteca',
        'mensagem': 'Acesse /api/livros/ para listar os livros em JSON e /admin/ para o Django Admin.'
    })


urlpatterns = [
    path('', inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('api/', include('livros.urls')),
]
