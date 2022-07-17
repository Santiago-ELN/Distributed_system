import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants

"""Carregar view de cadastro"""
def cadastro(request):
    if(request.method == "GET"):
        if(request.user.is_authenticated):
            return redirect('/dashboard/buscar')
        return render(request, 'cadastro.html')
    elif(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')
        if not password == confirmar_senha:
            messages.add_message(request, constants.ERROR, "As senhas não coincidem!")
            return redirect('/autenticacao/cadastro')
        if len(username.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(request, constants.ERROR, "Usuário e/ou senha não podem ficar vazios!")
            return redirect('/autenticacao/cadastro')
        user = User.objects.filter(username = username)
        if(user.exists()):
            messages.add_message(request, constants.ERROR, "O usuário já está cadastrado!")
            return redirect('/autenticacao/cadastro')
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            auth.login(request, user)
            return redirect('/dashboard')
        except:
            messages.add_message(request, "Ops! Algum erro aconteceu. Tente novamente mais tarde.")
            return redirect('/autenticacao/cadastro')
    
"""Carregar view de login"""
def login(request):
    if(request.method == "GET"):
        if(request.user.is_authenticated):
            return redirect('/dashboard/buscar')
        return render(request, 'login.html')
    elif(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if (len(username.split()) == 0) or (len(password.split()) == 0):
            messages.add_message(request, constants.ERROR,"Por favor, preencha todos os campos!")
            return redirect('/autenticacao/login')
        else:
            user = auth.authenticate(username = username, password = password)
            if not user:
                messages.add_message(request, constants.ERROR, "Usuário ou senha incorretos!")
                return redirect('/autenticacao/login')
            else:
                auth.login(request, user)
                return redirect('/dashboard/buscar')

def exit(request):
    auth.logout(request)
    return redirect('/autenticacao/login')
