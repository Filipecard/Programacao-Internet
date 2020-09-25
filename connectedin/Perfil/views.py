from django.shortcuts import render , redirect, get_object_or_404
from Perfil.models import Perfil

def index(request):
    return render(request, 'index.html',{'perfis':Perfil.objects.all()})

def exibir_perfil(request,id):
    perfil = get_object_or_404(Perfil,pk=id)
    return render(request,'perfil.html',{'perfil':perfil})

def convidar(request,id):
    perfil_a_convidar = Perfil.objects.get(id=id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('/')


def get_perfil_logado(request):
    return Perfil.objects.get(id=1)