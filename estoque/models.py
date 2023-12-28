from django.db import models
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
    data = models.DateField(auto_now_add=True, null=True, blank=True)
    descricao = models.TextField(null=False, blank=False)


    def __str__(self):
        return f"Produto [nome_produto={self.nome}]"
