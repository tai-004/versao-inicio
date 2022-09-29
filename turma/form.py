from .models import Turma
from django.forms import ModelForm
from .models import Altu

class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = "__all__"


class AltuForm(ModelForm):
    class Meta:
        model = Altu
        fields = "__all__"

