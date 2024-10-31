from django.contrib import admin
from .models import Dados, Contato, Experiencia, Formacao, Curriculo


@admin.register(Curriculo)
class CurriculoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "data_envio",
        "dados__nome",
        "dados__data_nasc",
        "dados__cpf",
        "contato__email",
        "contato__telefone",
        "contato__endereco",
        "contato__cidade",
        "contato__estado",
        "contato__cep",
        "experiencia__cargo",
        "experiencia__empresa",
        "experiencia__data_inicio",
        "experiencia__data_fim",
        "formacao__curso",
        "formacao__instituicao",
        "formacao__data_inicio",
        "formacao__data_fim",
    )

    search_fields = ("dados__nome",)


@admin.register(Dados)
class DadosAdmin(admin.ModelAdmin):
    list_display = ("nome", "data_nasc", "cpf")


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ("email", "telefone", "endereco", "cidade", "estado", "cep")


@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ("cargo", "empresa", "data_inicio", "data_fim")


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("curso", "instituicao", "data_inicio", "data_fim")
