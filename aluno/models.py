from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
class Aluno(models.Model):
    matricula = models.CharField (max_length=20)
    situacao = models.CharField (max_length= 10)

    def __str__(self):
        return self.matricula + "\n" + self.situacao
