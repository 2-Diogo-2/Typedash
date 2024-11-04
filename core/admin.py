from django.contrib import admin
from .models import HistoricoTeste, ResultadosTeste, Dicas, CustomUser

# Registre o modelo CustomUser no painel admin se ele for utilizado como modelo de autenticação personalizado
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username']
    search_fields = ['email', 'username']

# Registre os outros modelos no painel admin
@admin.register(HistoricoTeste)
class HistoricoTestesAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'erros', 'tempo_total', 'data']
    search_fields = ['usuario__username', 'data']
    list_filter = ['usuario', 'data']

@admin.register(ResultadosTeste)
class ResultadosTesteAdmin(admin.ModelAdmin):
    list_display = ['teste', 'frase', 'tempo_gasto', 'erros']
    search_fields = ['teste__usuario__username', 'frase']
    list_filter = ['teste', 'frase']

@admin.register(Dicas)
class DicasAdmin(admin.ModelAdmin):
    list_display = ['texto', 'imagem']
    search_fields = ['texto']
