import unittest
from django.urls import reverse
from django.test import Client
from .models import Empresa
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_empresa(**kwargs):
    defaults = {}
    defaults["nomeFantasia"] = "nomeFantasia"
    defaults["cnpj"] = "cnpj"
    defaults["qnt_funcionarios"] = "qnt_funcionarios"
    defaults["cidade"] = "cidade"
    defaults["estado"] = "estado"
    defaults["nome_completo"] = "nome_completo"
    defaults["login"] = "login"
    defaults["senha"] = "senha"
    defaults["nomeFantasia"] = "nomeFantasia"
    defaults["nome_fornecedor"] = "nome_fornecedor"
    defaults["alimentos"] = "alimentos"
    defaults["quantidade"] = "quantidade"
    defaults["valor"] = "valor"
    defaults["peso"] = "peso"
    defaults["refeicoes"] = "refeicoes"
    defaults["data"] = "data"
    defaults["id_refeicao"] = "id_refeicao"
    defaults["qnt_func"] = "qnt_func"
    defaults["preferencia"] = "preferencia"
    defaults["menos_gosta"] = "menos_gosta"
    defaults.update(**kwargs)
    return Empresa.objects.create(**defaults)


class EmpresaViewTest(unittest.TestCase):
    '''
    Tests for Empresa
    '''

    def setUp(self):
        self.client = Client()

    def test_list_empresa(self):
        url = reverse('app_name_empresa_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_empresa(self):
        url = reverse('app_name_empresa_create')
        data = {
            "nomeFantasia": "nomeFantasia",
            "cnpj": "cnpj",
            "qnt_funcionarios": "qnt_funcionarios",
            "cidade": "cidade",
            "estado": "estado",
            "nome_completo": "nome_completo",
            "login": "login",
            "senha": "senha",
            "nomeFantasia": "nomeFantasia",
            "nome_fornecedor": "nome_fornecedor",
            "alimentos": "alimentos",
            "quantidade": "quantidade",
            "valor": "valor",
            "peso": "peso",
            "refeicoes": "refeicoes",
            "data": "data",
            "id_refeicao": "id_refeicao",
            "qnt_func": "qnt_func",
            "preferencia": "preferencia",
            "menos_gosta": "menos_gosta",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_empresa(self):
        empresa = create_empresa()
        url = reverse('app_name_empresa_detail', args=[empresa.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_empresa(self):
        empresa = create_empresa()
        data = {
            "nomeFantasia": "nomeFantasia",
            "cnpj": "cnpj",
            "qnt_funcionarios": "qnt_funcionarios",
            "cidade": "cidade",
            "estado": "estado",
            "nome_completo": "nome_completo",
            "login": "login",
            "senha": "senha",
            "nomeFantasia": "nomeFantasia",
            "nome_fornecedor": "nome_fornecedor",
            "alimentos": "alimentos",
            "quantidade": "quantidade",
            "valor": "valor",
            "peso": "peso",
            "refeicoes": "refeicoes",
            "data": "data",
            "id_refeicao": "id_refeicao",
            "qnt_func": "qnt_func",
            "preferencia": "preferencia",
            "menos_gosta": "menos_gosta",
        }
        url = reverse('app_name_empresa_update', args=[empresa.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
