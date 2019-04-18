from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    foto = models.ImageField()
    texto = models.TextField()

    def summary(self):
        return self.texto[0:100]