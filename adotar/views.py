
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import PedidoAdocao
from divulgar.models import Pet, Raca
from adotar.models import PedidoAdocao
from django.core.mail import send_mail

# Create your views here.





def listar_pets(request):
    if request.method == "GET":
        #pets = Pets.objects.filter(status='P')
        pets = Pet.objects.all()
        raca = Raca.objects.all()


        bairro = request.GET.get('bairro')
        raca_filter = request.GET.get('raca')

        if bairro:
            pets = pets.filter(bairro__icontains=bairro)

        if raca_filter:
            pets = pets.filter(raca__id=raca_filter)
            raca_filter = Raca.objects.get(id=raca_filter)
        return render(request, 'listar_pets.html', {'pets': pets, 'racas': raca, 'raca_filter': raca_filter,})


@login_required
def pedido_adocao(request, id_pet):
    pet = Pet.objects.filter(id=id_pet, status="p").first()
    
    if not pet:
        messages.add_message(request, constants.ERROR, 'Esse pet já foi adotado :)')
        return redirect('/adotar')
    
    pedido = PedidoAdocao(pet=pet, usuario=request.user, data=datetime.now())
    pedido.save()
    
    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção realizado, você receberá um e-mail caso ele seja aprovado.')
    return redirect('/adotar')




def processa_pedido_adocao(request, id_pedido):
    status = request.GET.get('status')
    pedido = PedidoAdocao.objects.get(id=id_pedido)
    if status == "A":
        pedido.status = 'AP'
        string = '''Olá, sua adoção foi aprovada. ...'''
    elif status == "R":
        string = '''Olá, sua adoção foi recusada. ...'''
        pedido.status = 'R'
    pedido.save()
    print(pedido.usuario.email)
    email = send_mail(
        'Sua adoção foi processada',
        string,
        'email@teste.com.br',
        [pedido.usuario.email,],
    )
    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção processado com sucesso')
    return redirect('/divulgar/ver_pedido_adocao')
