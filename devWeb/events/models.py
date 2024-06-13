from django.db import models

class Certificado(models.Model):
    nome = models.CharField(max_length=100)
    carga = models.IntegerField()
    
class Evento(models.Model):
    nome = models.CharField(max_length=100)
    description = models.TextField()
    qtdInscritos = models.IntegerField()
    certificadoEvento = models.ForeignKey(Certificado, on_delete=models.SET_NULL, null=True)
    dataEvento = models.DateField()
    
