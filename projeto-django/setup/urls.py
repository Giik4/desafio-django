from django.contrib import admin
from django.urls import path

from curriculos.views import curriculo_list, cadastro, save, visualizar

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", cadastro, name="cadastro"),
    path("lista_curriculos", curriculo_list, name="lista"),
    path("redirect", save, name="redirect"),
    path("visualizar/<int:id>", visualizar, name="visualizar"),
    # path("deletar/<int:id>", deletar, name="deletar"),
]
