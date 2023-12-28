from django.shortcuts import render
from estoque.models import Produtos



def index(request):
    return render(request, 'estoque/index.html')

def estoque(request):
    produtos = Produtos.objects.order_by("data")

    return render(request, 'estoque/estoque.html', {"estoque": produtos})

def cliente(request):
    return render(request, 'estoque/cliente.html')

def adicionar_estoque(request):
    return render(request, 'estoque/adicionar_estoque.html')


def novo_cliente(request):
    return render(request, 'estoque/novo_cliente.html')


def buscar(request):
    produtos = Produtos.objects.all()
    if "buscar" in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            produtos = produtos.filter(nome__icontains=nome_buscar)


    return render(request, "estoque/buscar.html", {"estoque": produtos})