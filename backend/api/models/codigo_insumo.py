from django.db import models

class codigo_insumo(models.Model):
     codigo_insumo = models.IntegerField(primary_key=True)
     def __str__(self): 
         return str(self.codigo_insumo)