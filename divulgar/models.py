from django.db import models
from django.contrib.auth.models import User


class Raca(models.Model):
    raca = models.CharField(max_length=50)



    def __str__(self):
        return self.raca


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    
    def __str__(self):
        return self.tag



class Pet(models.Model):
    choices_status = (('P', 'Para adoção'), ('A', 'Adotado'))
    
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to="fotos_pets")
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    bairro = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    tags = models.ManyToManyField(Tag)
    raca = models.ForeignKey(Raca, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=choices_status, default='P')


    def __str__(self):
        return self.nome
