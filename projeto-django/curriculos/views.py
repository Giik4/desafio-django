from django.shortcuts import render, redirect
from .models import Curriculo, Dados, Contato, Experiencia, Formacao


def cadastro(request):
    return render(request, "curriculos/curriculo_create.html")


def save(request):
    d = Dados()
    d.nome = request.POST.get("nome")
    d.data_nasc = request.POST.get("dataNasc")
    d.cpf = request.POST.get("cpf")
    d.save()

    c = Contato()
    c.email = request.POST.get("email")
    c.telefone = request.POST.get("telefone")
    c.endereco = request.POST.get("endereco")
    c.cidade = request.POST.get("cidade")
    c.estado = request.POST.get("estado")
    c.cep = request.POST.get("cep")
    c.save()

    e = Experiencia()
    e.cargo = request.POST.get("cargo")
    e.empresa = request.POST.get("empresa")
    e.data_inicio = request.POST.get("dataExpIni")
    e.data_fim = request.POST.get("dataExpFim")
    e.save()

    f = Formacao()
    f.curso = request.POST.get("curso")
    f.instituicao = request.POST.get("instituicao")
    f.data_inicio = request.POST.get("dataForIni")
    f.data_fim = request.POST.get("dataForFim")
    f.save()

    curriculo = Curriculo(dados=d, contato=c, experiencia=e, formacao=f)
    curriculo.save()

    return render(request, "curriculos/curriculo_redirect.html")


def visualizar(request, id):
    curriculo = Curriculo.objects.get(id=id)
    return render(request, "curriculos/curriculo_view.html", {"curriculo": curriculo})


# def deletar(request,id):
#     curriculo = Curriculo.objects.get(id=id)
#     curriculo.delete()
#     return redirect(curriculo_list)


def curriculo_list(request):
    curriculos = Curriculo.objects.all()
    return render(request, "curriculos/curriculo_list.html", {"curriculos": curriculos})
