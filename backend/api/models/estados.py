from django.db import models

class estados(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)
    def __str__(self):
        return self.sigla