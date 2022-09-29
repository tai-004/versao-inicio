from se.form import CursoForm

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Curso

#criar curso
def criar(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/se/post/") 
    else: 
        form = CursoForm()
    context = {
            'form': form
        }
    return render(request, 'se/criar.html', context)

def index(request):
    return render(request, "se/index.html", {})

#atualizar dados do curso
def editar(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    
    if request.method == "POST":
        form = Curso(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/se/post/")
    else:    
        form = CursoForm(instance=curso)
    
    context = {
        'form': form,
        'curso_id': curso_id
    }
    
    return render(request, 'se/editar.html', context)

def excluir(request, curso_id):
    
    Curso.objects.get(pk=curso_id).delete()
    
    return HttpResponseRedirect("/se/post/")

def post(request):
    curso = Curso.objects.all()
    context = {
        'curso': curso
    }
    
    return render(request, 'se/post.html', context)

#método para detalhar pessoas
def detail(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    context = {
        'curso': curso
    }
    
    return render(request, 'se/detail.html', context)
