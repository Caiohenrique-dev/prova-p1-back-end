from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=120)
    nacionalidade = models.CharField(max_length=80)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
