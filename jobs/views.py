from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Jobs

@login_required(login_url='/auth/login')
def buscar_jobs(request):
    if request.method == "GET":
        preco_minimo = request.GET.get('preco_minimo')
        preco_maximo = request.GET.get('preco_maximo')

        prazo_minimo = request.GET.get('prazo_minimo')
        prazo_maximo = request.GET.get('prazo_maximo')

        categoria = request.GET.get('categoria')

        if preco_minimo or preco_maximo or prazo_minimo or prazo_maximo or categoria:
            if not preco_minimo:
                preco_minimo = 0

            if not preco_maximo:
                preco_maximo = 999999

            if not prazo_minimo:
                prazo_minimo = datetime.today()

            if not prazo_maximo:
                prazo_maximo = datetime(year=3000, month=1, day=1)

            categoria = [categoria, ]
            jobs = Jobs.objects.filter(preco__gte=preco_minimo)\
                .filter(preco__lte=preco_maximo)\
                .filter(prazo_entrega__gte=prazo_minimo)\
                .filter(prazo_entrega__lte=prazo_maximo)\
                .filter(categoria__in=categoria)\
                .filter(reservado=False)
        else:
            jobs = Jobs.objects.filter(reservado=False)

        return render(request, 'find_jobs.html', {'jobs': jobs})
@login_required(login_url='/auth/login')
def aceitar_job(request, id):
    job = Jobs.objects.get(id=id)
    job.profissional = request.user
    job.reservado = True
    job.save()
    return redirect(buscar_jobs)
@login_required(login_url='/auth/login')
def perfil(request):
    if request.method == "GET":
        jobs = Jobs.objects.filter(profissional=request.user)
        return render(request, 'perfil.html', {'jobs': jobs})
       
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')

        usuario = User.objects.filter(username=username).exclude(id=request.user.id)

        if usuario.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário cadastrado com esse nome')
            return redirect('/jobs/perfil')

        usuario = User.objects.filter(email=email).exclude(id=request.user.id)

        if usuario.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse e-mail')
            return redirect('/jobs/perfil')
        
        request.user.username = username
        request.user.email = email
        request.user.first_name = primeiro_nome
        request.user.last_name = ultimo_nome
        request.user.save()
        messages.add_message(request, constants.SUCCESS, 'Dados alterados com sucesso!')
        return redirect('/jobs/find_jobs')
@login_required(login_url='/auth/login')
def enviar_projeto(request):
    arquivo = request.FILES.get('file')
    id_job = request.POST.get('id')

    job = Jobs.objects.get(id=id_job)

    job.arquivo_final = arquivo
    job.status = 'AA'
    job.save()
    return redirect('/jobs/perfil')
