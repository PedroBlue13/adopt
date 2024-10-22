from django.shortcuts import render
from divulgar.models import Pet, Raca

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
        return render(request, 'listar_pets.html', {'pets': pets, 'racas': raca, 'raca_filter': raca_filter,})