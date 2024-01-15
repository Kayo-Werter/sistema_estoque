from django.contrib import admin
from estoque.models import Produtos, Cliente, Endereco

class ListandoProdutos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'quantidade', 'tamanho', 'descricao')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ("tamanho",)
    list_per_page = 10


class ListandoClientes(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone')


class ListandoEnderecos(admin.ModelAdmin):
    list_display = ('cep', 'logradouro', 'bairro')


admin.site.register(Produtos, ListandoProdutos)
admin.site.register(Cliente, ListandoClientes)
admin.site.register(Endereco, ListandoEnderecos)