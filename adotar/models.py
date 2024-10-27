from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from divulgar.models import Pet
from django.contrib.auth.models import User

# Create your models here.
class PedidoAdocao(models.Model):
    choices_status = (
        ('AG', 'Aguardando Aprovação'),
        ('AP', 'Aguardando Aprovação'),
        ('R', 'Aguardando Aprovação'),
    )

    #crie uma model com os campos pet, usuario, data, status
    pet = models.ForeignKey(Pet, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = models.DateField()
    status = models.CharField(max_length=2, choices=choices_status, default='AG')
>>>>>>> f2a86fb (page see pet, bug fix database)
