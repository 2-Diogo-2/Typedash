from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import (
    login_view,
    teste_view,
    dicas_view,
    home_view,
    armazenar_resultados,
    exibir_historico,
    finalizar_teste,
    perfil,
    editar_login_view,
    excluir_login_view,
    resultados_view,
    salvar_resultados,  # Importe a nova view para salvar resultados
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('teste/', teste_view, name='teste'),
    path('dicas/', dicas_view, name='dicas'),
    path('armazenar_resultados/', armazenar_resultados, name='armazenar_resultados'),
    path('historico/', exibir_historico, name='historico'),
    path('finalizar_teste/', finalizar_teste, name='finalizar_teste'),
    path('perfil/', perfil, name='perfil'),
    path('editar_login/', editar_login_view, name='editar_login'),
    path('excluir_login/', excluir_login_view, name='excluir_login'),
    path('resultados/', resultados_view, name='resultados'),
    path('salvar_resultados/', salvar_resultados, name='salvar_resultados'),
    path('', home_view, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
