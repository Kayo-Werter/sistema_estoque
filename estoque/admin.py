from django.contrib import admin
from estoque.models import Produtos

class ListandoProdutos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'quantidade', 'tamanho', 'descricao')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ("tamanho",)
    list_per_page = 10

admin.site.register(Produtos, ListandoProdutos)
