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
            return redirect('/jobs/buscar_jobs')
        return render(request, 'cadastro.html')
    elif(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')
        if not password == confirmar_senha:
            messages.add_message(request, constants.ERROR, "As senhas não coincidem!")
            return redirect('/auth/cadastro')
        if len(username.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(request, constants.ERROR, "Usuário e/ou senha não podem ficar vazios!")
            return redirect('/auth/cadastro')
        user = User.objects.filter(username = username)
        if(user.exists()):
            messages.add_message(request, constants.ERROR, "O usuário já está cadastrado!")
            return redirect('/auth/cadastro')
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('/auth/login')
        except:
            return redirect('/auth/cadastro')
    
"""Carregar view de login"""
def login(request):
    if(request.method == "GET"):
        if(request.user.is_authenticated):
            return redirect('/jobs/buscar_jobs')
        return render(request, 'login.html')
    elif(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        if (len(username.split()) == 0) or (len(password.split()) == 0):
            messages.add_message(request, constants.ERROR,"Por favor, preencha todos os campos!")
            return redirect('/auth/login')
        else:
            user = auth.authenticate(username = username, password = password)
            if not user:
                messages.add_message(request, constants.ERROR, "Usuário ou senha incorretos!")
                return redirect('/auth/login')
            else:
                auth.login(request, user)
                return redirect('/jobs/buscar_jobs')

def exit(request):
    auth.logout(request)
    return redirect('/auth/login')
