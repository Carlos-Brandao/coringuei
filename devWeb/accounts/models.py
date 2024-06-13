from django.db import models
from events.models import Certificado

class Usuario(models.Model):
    nome = models.CharField(max_length=15)  
    email = models.EmailField()
    senha = models.CharField(max_length=20)
    funcao = models.BooleanField()
    certificados = models.ForeignKey(Certificado, on_delete=models.SET_NULL, null=True)
    
    