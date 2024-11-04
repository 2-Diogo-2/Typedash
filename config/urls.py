from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import salvar_resultado_teste

from core.views import (
    login_view,
    teste_view,
    dicas_view,
    home_view,
    salvar_resultado_teste,  # Nome corrigido para salvar resultados de teste
    exibir_historico,
    finalizar_teste,
    perfil,
    excluir_login_view,
    resultados_view,
    register,  # Importa a view de registro
    edit_user,  # Importa a view de edição de usuário
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('teste/', teste_view, name='teste'),
    path('dicas/', dicas_view, name='dicas'),
    path('salvar_resultado/', salvar_resultado_teste, name='salvar_resultado'),  # Corrigido para salvar_resultado_teste
    path('historico/', exibir_historico, name='historico_testes'),  # Mudando o nome para 'historico_testes'
    path('finalizar_teste/', finalizar_teste, name='finalizar_teste'),
    path('perfil/', perfil, name='perfil'),
    path('excluir_login/', excluir_login_view, name='excluir_login'),
    path('resultados/', resultados_view, name='resultados'),
    path('register/', register, name='register'),  # URL para registro
    path('edit_user/', edit_user, name='edit_user'),  # URL para edição de usuário
    path('', home_view, name='home'),  # URL principal (home)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
