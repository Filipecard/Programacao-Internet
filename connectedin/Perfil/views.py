from django.shortcuts import render , redirect, get_object_or_404
from Perfil.models import Perfil,Convite

def index(request):
    return render(request, 'index.html',{'perfil':Perfil.objects.all(),'perfil_logado':get_perfil_logado(request)})

def exibir_perfil(request,id):
    perfil = get_object_or_404(Perfil,pk=id)
    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()

    return render(request,'perfil.html',{'perfil':perfil,'perfil_logado':get_perfil_logado(request),'ja_eh_contato':ja_eh_contato})

def convidar(request,id):
    perfil_a_convidar =  get_object_or_404(Perfil,pk=id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('/')


def get_perfil_logado(request):
    return  get_object_or_404(Perfil,pk=1)

def aceitar(request,convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')