from django.db import models


class Dados(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nasc = models.DateField(null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)


class Contato(models.Model):
    email = models.CharField(max_length=50, null=False, blank=False)
    telefone = models.CharField(max_length=20, null=False, blank=False)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)
    cep = models.CharField(max_length=9, null=True, blank=True)


class Experiencia(models.Model):
    cargo = models.CharField(max_length=100, null=True, blank=True)
    empresa = models.CharField(max_length=100, null=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)


class Formacao(models.Model):
    curso = models.CharField(max_length=50, null=True, blank=True)
    instituicao = models.CharField(max_length=100, null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)


class Curriculo(models.Model):
    dados = models.OneToOneField(Dados, on_delete=models.PROTECT)
    contato = models.OneToOneField(Contato, on_delete=models.PROTECT)
    experiencia = models.OneToOneField(Experiencia, on_delete=models.PROTECT)
    formacao = models.OneToOneField(Formacao, on_delete=models.PROTECT)
    data_envio = models.DateTimeField(auto_now_add=True, null=False, blank=False)
