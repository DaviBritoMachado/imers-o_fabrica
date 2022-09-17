from django.db import models

# Create your models here.

class Produto(models.Model):
    titulo = models.CharField(max_length=80)
    valor = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    conteudo = models.TextField()
    date_publicacao = models.DateField(auto_now_add=True)

