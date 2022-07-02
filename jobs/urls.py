from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', lambda req: redirect(views.buscar_jobs)),
    path('buscar/', views.buscar_jobs, name='find_jobs'),
    path('aceitar/<int:id>/', views.aceitar_job, name="aceitar_job"),
    path('perfil/', views.perfil, name="perfil"),
    path('enviar-projeto/', views.enviar_projeto, name="enviar_projeto"),
]