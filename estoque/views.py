from django.shortcuts import render

def index(request):
    return render(request, 'estoque/index.html')

def estoque(request):
    return render(request, 'estoque/estoque.html')

def cliente(request):
    return render(request, 'estoque/cliente.html')

def adicionar_estoque(request):
    return render(request, 'estoque/adicionar_estoque.html')


def novo_cliente(request):
    return render (request, 'estoque/novo_cliente.html')