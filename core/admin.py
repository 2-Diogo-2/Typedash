from django.contrib import admin
from .models import HistoricoTeste

@admin.register(HistoricoTeste)
class HistoricoTestesAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'tempo_total', 'erros_total', 'data_teste']
    search_fields = ['usuario__username', 'data_teste']
    list_filter = ['data_teste']
