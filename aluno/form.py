from .models import Aluno
from django.forms import ModelForm

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = "__all__"

