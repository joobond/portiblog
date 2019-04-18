from django.db import models

class Job(models.Model):
    descricao = models.CharField(max_length=200)
    foto = models.ImageField()