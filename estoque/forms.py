from django import forms
from estoque.models import Produtos, Cliente


class FormProdutos(forms.ModelForm):
    class Meta:
        model = Produtos
        exclude = ['descricao',]
        labels = {
            'quantidade': "Quantidade",
            'nome': "Nome do Produto",
            'tamanho': "Tamanho",
            'data': "Data de Chegada"
        }
        
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control","placeholder": "Usuário"}),
            "quantidade": forms.NumberInput(attrs={"class": "form-control"}),
            "tamanho": forms.Select(attrs={"class": "form-select"}),
            "data": forms.DateInput(attrs={"class": "form-control", "type": "date"})
         }
        

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['',]
        labels = {
            "nome": "Cliente",
            "cpf": "CPF",
            "telefone": "Telefone",
            "cep": "CEP",
            "logradouro": "Logradouro",
            "numero": "Número",
            "complemento": "Complemento",
            "bairro": "Bairro",
            "cidade": "Cidade",
            "cep": "CEP",
            "logradouro": "Logradouro",
            "numero": "Número",
            "complemento": "Complemento",
            "bairro": "Bairro",
            "cidade": "Cidade"
        }

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome"}),
            "cpf": forms.TextInput(attrs={"class": "form-control", "placeholder": "CPF"}),
            "telefone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Telefone"}),
            "cep": forms.TextInput(attrs={"class": "form-control", "placeholder": "CEP"}),
            "logradouro": forms.TextInput(attrs={"class": "form-control", "placeholder": "Logradouro"}),
            "numero": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Número"}),
            "complemento": forms.TextInput(attrs={"class": "form-control", "placeholder": "Complemento"}),
            "bairro": forms.TextInput(attrs={"class": "form-control", "placeholder": "Bairro"}),
            "cidade": forms.TextInput(attrs={"class": "form-control", "placeholder": "Cidade"})
        }      


# from django import forms

# class FormProdutos(forms.Form):

#     TAMANHOS_DISPONIVEIS = [
#         ("pp", "PP"),
#         ("p", "P"),
#         ("m", "M"),
#         ("g", "G"),
#         ("gg", "GG"),
#         ("xg", "XG"),
#     ]

#     nome_produto=forms.CharField(
#         label="Nome do Produto",
#         required=True,
#         max_length=100,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Usuário"
#             }
#         ))

#     quantidade = forms.IntegerField(
#         label="Quantidade",
#         required=True,
#         min_value=0,
#         widget= forms.NumberInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Quantidade"
#             }
#         ))
    
#     tamanho = forms.ChoiceField(
#         choices=TAMANHOS_DISPONIVEIS,
        
#         widget = forms.Select(
#             attrs={
#                 "class": "form-select"
#             }
#         )
#     )

#     data_chegada = forms.DateField(
#         label="Data de Chegada",
#         widget= forms.DateInput(
#             attrs={
#                 "class": "form-control",
#                 "type": "date"
#             }
#         )   )

