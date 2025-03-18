from django.db import models

class insumos(models.Model):
    classificação = models.CharField(max_length=100)
    codigo_insumo = models.ForeignKey("/codigo_insumo" ,unique=True, on_delete=models.CASCADE, primary_key=True)
    descrição_insumo = models.TextField()
    unidade = models.CharField(max_length=50)
    origem_preço = models.CharField(max_length=2)
    def __str__(self):
        return self.descrição_insumo