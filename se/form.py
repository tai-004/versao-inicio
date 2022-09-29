from .models import Curso
from django.forms import ModelForm

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"