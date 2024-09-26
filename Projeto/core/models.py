from django.db import models
from django.contrib.auth.models import User

class ResultadosTeste(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    acertos = models.IntegerField()
    erros = models.IntegerField()
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
    texto = models.CharField(max_length=255)
    tempo = models.CharField(max_length=50)
    erros = models.IntegerField()
    data_realizacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Teste de {self.usuario.username} - {self.data_realizacao}"

class Dica(models.Model):
    texto = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='imgs/')  # Diretório onde as imagens serão armazenadas

    def __str__(self):
        return self.texto