<<<<<<< HEAD
from django.shortcuts import render
from divulgar.models import Pet, Raca
=======
from django.shortcuts import render, redirect, get_object_or_404
from divulgar.models import Pet, Raca
from django.contrib.messages import constants
from django.contrib import messages
from .models import PedidoAdocao
from datetime import datetime
from django.contrib.auth.decorators import login_required
>>>>>>> f2a86fb (page see pet, bug fix database)

# Create your views here.




def listar_pets(request):
    if request.method == "GET":
        # pets = Pets.objects.filter(status='P')
        pets = Pet.objects.all()
        raca = Raca.objects.all()


        bairro = request.GET.get('bairro')
        raca_filter = request.GET.get('raca')

        if bairro:
            pets = pets.filter(bairro_icontains=bairro)

        if raca_filter:
            pets = pets.filter(raca__id=raca_filter)
            raca_filter = Raca.objects.get(id=raca_filter)
<<<<<<< HEAD
        return render(request, 'listar_pets.html', {'pets': pets, 'racas': raca, 'raca_filter': raca_filter,})
=======
        return render(request, 'listar_pets.html', {'pets': pets, 'racas': raca, 'raca_filter': raca_filter,})


@login_required
def pedido_adocao(request, id_pet):
    pet = get_object_or_404(Pet, id=id_pet, status="p")

    # Cria o pedido de adoção
    pedido = PedidoAdocao(pet=pet, usuario=request.user, data=datetime.now())
    pedido.save()

    # Exibe mensagem de sucesso
    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção realizado, você receberá um e-mail caso ele seja aprovado.')
    return redirect('/adotar')
>>>>>>> f2a86fb (page see pet, bug fix database)
