from django.db import models
from django.contrib.auth.models import User
from django.db.models import BooleanField


class Pet(models.Model):

   nome= models.ForeignKey(User,on_delete=models.CASCADE)
   cpf = models.CharField(max_length=11)
   cidade = models.CharField(max_length=100)
   descricao = models.TextField()
   Telefone = models.CharField(max_length=11)
   email =models.EmailField()
   horario_data_criacao = models.DateTimeField(auto_now_add=True)
   foto = models.ImageField()
   ativo= models.BooleanField(default=True)


def __str__(self):
   return self.id


class Meta:
   db_table ='controle pet'