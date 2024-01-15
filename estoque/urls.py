from django.urls import path
from estoque.views import index, estoque, cliente, adicionar_produto, novo_cliente, buscar, produto

urlpatterns = [
    path('', index, name='index'),
    path('estoque/', estoque, name='estoque'),
    path('cliente/', cliente, name='cliente'),
    path('adicionar_produto/', adicionar_produto, name='adicionar_produto'),
    path('novo_cliente/', novo_cliente, name='novo_cliente'),
    path('buscar', buscar, name='buscar'),
    path('produto', produto, name='produto'),


]
