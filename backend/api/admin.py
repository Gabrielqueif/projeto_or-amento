from django.contrib import admin
from .models import insumos, estados, tabela
# Register your models here.
admin.site.register(insumos)
admin.site.register(estados)
admin.site.register(tabela)
# Compare this snippet from backend/api/views.py:
# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import insumos, estados, tabela
# from .serializers import insumosSerializer, estadosSerializer, tabelaSerializer
