from django import forms
from .models import Empresa


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('nomeFantasia', 'cnpj', 'qnt_funcionarios',
                  'cidade', 'estado', 'nome_completo', 'login',
                  'senha', 'nomeFantasia', 'nome_fornecedor',
                  'alimentos', 'quantidade', 'valor', 'peso',
                  'refeicoes', 'data', 'id_refeicao', 'qnt_func',
                  'preferencia', 'menos_gosta'
                  )
