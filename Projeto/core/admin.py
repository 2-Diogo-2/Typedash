from django.contrib import admin
from .models import ResultadosTeste, Dicas, HistoricoTeste  # Certifique-se de importar o modelo HistoricoTeste

admin.site.register(ResultadosTeste)
admin.site.register(Dicas)
admin.site.register(HistoricoTeste)  # Adicione esta linha
