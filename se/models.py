from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class Curso(models.Model):
    codigo= models.IntegerField(default=20)
    descricao = models.CharField(max_length=100)

   
    def __str__(self):
        return self.descricao
        