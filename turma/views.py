from django.shortcuts import render
from turma.form import AltuForm
from turma.form import TurmaForm
from django.http import HttpResponseRedirect
from .models import Turma
from .models import Altu
def index(request):
    return render(request, "turma/index.html", {})

def cadrastrar(request):
    if request.method == "POST":
        form = AltuForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/turma/post1/") 
    else: 
        form = AltuForm()
    context = {
            'form': form
        }
    return render(request, 'turma/index.html', context)

def criar(request):
    if request.method == "POST":
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/aluno/post/") 
    else: 
        form = TurmaForm()
    context = {
            'form': form
        }
    return render(request, 'turma/criar.html', context)

def post(request):
    turma = Turma.objects.all()
    context = {
        'turma': turma
    }
    
    return render(request, 'aluno/post.html', context)

def post1(request):
    altu = Altu.objects.all()
    context = {
        'altu': altu
    }
    
    return render(request, 'turma/post.html', context)