from django.urls import path
from . import views

app_name = 'livros'

urlpatterns = [
    path('livros/', views.listar_livros, name='listar_livros'),
]
