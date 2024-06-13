from django.db import models

class Trabalho(models.Model):
    diaPostado = models.DateField()
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    nota = models.IntegerField()
    comentario = models.TextField()