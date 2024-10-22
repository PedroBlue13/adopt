from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome').strip()
        email = request.POST.get('email').strip()
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Verificar se algum campo está vazio
        if not nome or not email or not senha or not confirmar_senha:
            messages.add_message(request, constants.ERROR, "Preencha todos os campos.")
            return render(request, 'cadastro.html')

        # Verificar se as senhas coincidem
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
            return render(request, 'cadastro.html')

        # Verificar se a senha tem pelo menos 6 caracteres
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, "A senha precisa ter mais de 6 caracteres.")
            return render(request, 'cadastro.html')

        # Verificar se o usuário já existe
        if User.objects.filter(username=nome).exists():
            messages.add_message(request, constants.ERROR, "Nome de usuário já está em uso, tente outro!")
            return render(request, 'cadastro.html')

        if User.objects.filter(email=email).exists():
            messages.add_message(request, constants.ERROR, "E-mail já está cadastrado.")
            return render(request, 'cadastro.html')

        # Tentar criar o usuário
        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            messages.add_message(request, constants.SUCCESS, "Parabéns, agora podemos falar de gatinhos!")
            return redirect(reverse('login'))  # Redireciona para a página de login.
        except Exception as e:
            messages.add_message(request, constants.ERROR, "Erro no sistema, tente novamente em breve! :( )")
            return render(request, 'cadastro.html')


def logar(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        nome = request.POST.get('nome').strip()
        senha = request.POST.get('senha')

        user = authenticate(username=nome, password=senha)

        if user is not None:
            login(request, user)
            return redirect('/divulgar/novo_pet')
        else:
            messages.add_message(request, constants.ERROR, "Usuário ou senha inválidos!")
            return render(request, 'login.html')


def sair(request):
    logout(request)
    return redirect('/auth/login')
