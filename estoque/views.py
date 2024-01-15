from django.shortcuts import render, redirect
from estoque.models import Produtos, Cliente
from django.contrib import messages
from estoque.forms import FormProdutos, FormCliente


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    return render(request, 'estoque/index.html')

def estoque(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    produtos = Produtos.objects.order_by("data")

    return render(request, 'estoque/estoque.html', {"estoque": produtos})

def cliente(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    clientes = Cliente.objects.order_by("nome")

    return render(request, 'estoque/cliente.html', {"clientes": clientes})

def produto(request):



    return render(request, 'estoque/produto.html')

def adicionar_produto(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    form = FormProdutos
    
    if request.method == 'POST':
        form = FormProdutos(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Produto cadastrado com sucesso!")
            return redirect('estoque')
    
    return render(request, 'estoque/adicionar_produto.html', {"form": form})

def novo_cliente(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    form_cliente = FormCliente
    
    if request.method == "POST":
        form_cliente = FormCliente(request.POST)
        
        if form_cliente.is_valid():
            form_cliente.save()
            
            messages.success(request, "Cliente Cadastrado com sucesso")
            return redirect('cliente')
    
    
    return render(request, 'estoque/novo_cliente.html', {"form_cliente": form_cliente})

def buscar(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    
    
    if "buscar" in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            produtos = produtos.filter(nome__icontains=nome_buscar)

    return render(request, "estoque/buscar.html", {"estoque": produtos})
