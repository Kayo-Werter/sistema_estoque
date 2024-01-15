from django.db import models
from datetime import date
# auto_now no DateTimeField permite atualização da data

class Produtos(models.Model):

    TAMANHOS_DISPONIVEIS = {
        ("P", "p"),
        ("PP", "pp"),
        ("M", "m"),
        ("G", "g"),
        ("GG", "gg"),
        ("XG", "xg"),
    }

    nome = models.CharField(max_length=100, null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False, default=0)
    tamanho = models.CharField(max_length=2, null=False, blank=False, choices=TAMANHOS_DISPONIVEIS, default='')
    data = models.DateField(default=date.today, blank=False)
    descricao = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"Produto [nome_produto={self.nome}]"
    


class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    telefone = models.CharField(max_length=11)


    def __str__(self):
        return f"Nome: {self.nome}"
    

class Endereco(models.Model):
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=30)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=8, null=True, blank=True)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return f"Nome: {self.cep}"

