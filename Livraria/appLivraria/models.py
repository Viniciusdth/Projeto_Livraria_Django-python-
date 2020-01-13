from django.db import models

class Empresa(models.Model):
    nomeFantasia = models.CharField(max_length=255, null=False, blank=False)
    cnpj = models.DecimalField(max_digits=10,decimal_places=2, null=False, blank=False)
    qnt_funcionarios = models.DecimalField(max_digits=10,decimal_places=2, null=False, blank=False)
    cidade = models.CharField(max_length=255, null=False, blank=False)
    estado = models.CharField(max_length=255, null=False, blank=False)
    nome_completo = models.CharField(max_length=255, null=False, blank=False)
    login = models.DecimalField(max_digits=10,decimal_places=2, null=False, blank=False)
    senha = models.CharField(max_length=255, null=False, blank=False)
    nome_fornecedor = models.CharField(max_length=255, null=False, blank=False)
    alimentos = models.CharField(max_length=255, null=False, blank=False)
    quantidade = models.DecimalField(max_digits=10,decimal_places=2, null=False, blank=False)
    valor = models.CharField(max_length=255, null=False, blank=False)
    peso = models.DecimalField(max_digits=10,decimal_places=2, null=False, blank=False)
    refeicoes = models.DecimalField(max_digits=10,decimal_places=2, null=False, blank=False)
    data = models.DateField(null=False, blank=False)
    id_refeicao = models.DecimalField(max_digits=10,decimal_places=2, null=False, blank=False)
    qnt_func = models.CharField(max_length=255, null=False, blank=False)
    preferencia = models.CharField(max_length=255, null=False, blank=False)
    menos_gosta = models.CharField(max_length=255, null=False, blank=False)


objetos = models.Manager()
