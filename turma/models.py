from django.db import models

# Create your models here.
class Turma(models.Model):
    
    turma = models.CharField(max_length=10, null=True)

    def __str__(self):
         return self.turma

    
class Altu(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING)
    aluno = models.ForeignKey("aluno.Aluno", on_delete=models.DO_NOTHING)

 
