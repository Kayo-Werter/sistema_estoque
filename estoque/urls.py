from django.urls import path
from estoque.views import index, estoque, cliente, adicionar_estoque, novo_cliente, buscar

urlpatterns = [
    path('', index, name='index'),
    path('estoque/', estoque, name='estoque'),
    path('cliente/', cliente, name='cliente'),
    path('adicionar_estoque/', adicionar_estoque, name='adicionar_estoque'),
    path('novo_cliente/', novo_cliente, name='novo_cliente'),
    path('buscar', buscar, name='buscar'),

    
]
