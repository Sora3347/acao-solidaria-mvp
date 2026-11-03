
from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    vencimento = models.DateField()

class Familia(models.Model):
    nome = models.CharField(max_length=150)
    recebeu_este_mes = models.BooleanField(default=False)
