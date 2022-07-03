from tabnanny import verbose
import django
from django.db import models
from django.contrib.auth.models import User

class Referencias(models.Model):
    titulo = models.CharField(max_length=32, blank=True, null=True)
    arquivo = models.FileField(upload_to='referencias')

    def __str__(self) -> str:
        return f'{self.titulo}'
    
    class Meta:
        verbose_name = 'Imagem de Referência'
        verbose_name_plural = 'Imagens de Referência'
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if not self.titulo:
            self.titulo = f"Imagem nº [{self.id}]"


class JobCategory(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Categoria de Serviço'
        verbose_name_plural = 'Categorias de Serviços'


class Jobs(models.Model):
    """"""
    status_choices = (('C', 'Em criação'),
                      ('AA', 'Aguardando aprovação'),
                      ('F', 'Finalizado'))

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True, default=None)
    prazo_entrega = models.DateField()
    hora_entrega = models.TimeField(blank=True, default=django.utils.timezone.now)
    preco = models.FloatField(default=00.00)
    referencias = models.ManyToManyField(Referencias, blank=True, help_text='Imagens de referência de qualidade para o trabalho')
    profissional = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, )
    reservado = models.BooleanField(default=False, help_text='Define se o trabalho está reservado para um profissional específico. Atualizado automaticamente.')
    status = models.CharField(max_length=2, choices=status_choices, default='C')
    arquivo_final = models.FileField(blank = True, null=True, help_text='Arquivo anexado para entrega pelo profissional')

    def __str__(self) -> str:
        return self.titulo
    
    class Meta:
        verbose_name ='Serviço'
        verbose_name_plural = 'Serviços'
