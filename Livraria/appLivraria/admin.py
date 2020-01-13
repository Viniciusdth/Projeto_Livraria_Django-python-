from django.contrib import admin
from django import forms
from .models import Empresa


class EmpresaAdminForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'


class EmpresaAdmin(admin.ModelAdmin):
    form = EmpresaAdminForm
    list_display = ['nomeFantasia', 'cnpj', 'qnt_funcionarios', 'cidade', 'estado', 'nome_completo', 'login', 'senha',
                    'nomeFantasia', 'nome_fornecedor', 'alimentos', 'quantidade', 'valor', 'peso', 'refeicoes', 'data',
                    'id_refeicao', 'qnt_func', 'preferencia', 'menos_gosta']
    readonly_fields = ['nomeFantasia', 'cnpj', 'qnt_funcionarios', 'cidade', 'estado', 'nome_completo', 'login',
                       'senha', 'nomeFantasia', 'nome_fornecedor', 'alimentos', 'quantidade', 'valor', 'peso',
                       'refeicoes', 'data', 'id_refeicao', 'qnt_func', 'preferencia', 'menos_gosta']


admin.site.register(Empresa, EmpresaAdmin)
