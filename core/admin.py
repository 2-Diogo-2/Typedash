from django.contrib import admin
from .models import HistoricoTeste

@admin.register(HistoricoTeste)
class HistoricoTestesAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'erros', 'tempo_total', 'data']  # Altere para 'erros' e 'data'
    search_fields = ['usuario__username', 'data']  # Ajuste para 'data' em vez de 'data_teste'
    list_filter = ['usuario', 'data']  # Corrija o filtro para 'data'
