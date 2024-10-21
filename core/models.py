from django.db import models
from django.contrib.auth.models import User

class ResultadosTeste(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    acertos = models.IntegerField(default=0)
    erros = models.IntegerField()
    tempo = models.FloatField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Resultado de {self.usuario.username} - {self.data}'

class Dicas(models.Model):
    texto = models.TextField()
    imagem = models.ImageField(upload_to='dicas_imagens/')

    def __str__(self):
        return f'Dica: {self.texto[:50]}...'

class HistoricoTeste(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    frases = models.TextField(blank=True, null=True)
    tempo_total = models.CharField(max_length=50)
    erros_total = models.IntegerField()
    data_teste = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Teste de {self.usuario.username} - {self.data_teste}"

