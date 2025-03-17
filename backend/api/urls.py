from django.urls import path
from . import views

urlpatterns = [
    path('insumos/', views.insumosList.as_view()),
    path('estados/', views.estadosList.as_view()),
    path('tabela/', views.tabelaList.as_view()),
]