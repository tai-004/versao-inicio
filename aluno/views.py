from django.shortcuts import render
from aluno.form import AlunoForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Aluno
def index(request):
    return render(request, "aluno/index.html", {})


#criar curso
def criar(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/aluno/post/") 
    else: 
        form = AlunoForm()
    context = {
            'form': form
        }
    return render(request, 'aluno/criar.html', context)

def post(request):
    aluno = Aluno.objects.all()
    context = {
        'aluno': aluno
    }
    
    return render(request, 'aluno/post.html', context)