from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Garantir que o email seja único

    USERNAME_FIELD = 'email'  # Use email como o campo de login
    REQUIRED_FIELDS = []  # Campos obrigatórios adicionais

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Adicionado
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Adicionado
        blank=True,
    )

class HistoricoTeste(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Atualizado para usar AUTH_USER_MODEL
    data = models.DateTimeField(auto_now_add=True)  # Define a data automaticamente
    erros = models.IntegerField(default=0)  # Valor padrão definido
    tempo_total = models.DurationField(default=timezone.timedelta(0))  # Alterado para DurationField
    palavras_por_minuto = models.FloatField(default=0.0)  # Alterado para FloatField e valor padrão definido

    def __str__(self):
        return f"{self.usuario.username} - {self.data}"

class ResultadosTeste(models.Model):
    teste = models.ForeignKey(HistoricoTeste, on_delete=models.CASCADE)  # Removido o default para forçar a relação
    frase = models.CharField(max_length=255, default='Digite aqui a sua frase')
    tempo_gasto = models.DurationField(default=timezone.timedelta(0))  # Valor padrão para 0 segundos
    erros = models.IntegerField()

    def __str__(self):
        return f'Resultado de {self.teste} - {self.frase}'

# Dicas para usuários
class Dicas(models.Model):
    texto = models.TextField()
    imagem = models.ImageField(upload_to='dicas_imagens/')

    def __str__(self):
        return f'Dica: {self.texto[:50]}...'
