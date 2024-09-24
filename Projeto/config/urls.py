from django.contrib import admin
from django.urls import path
from core.views import (
    login_view,
    teste_view,
    dicas_view,
    home_view,
    armazenar_resultados,
    exibir_historico,
    finalizar_teste,
    perfil,
)

# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),  # URL de login
    path('teste/', teste_view, name='teste'),  # URL para o teste
    path('dicas/', dicas_view, name='dicas'),  # URL para dicas
    path('armazenar_resultados/', armazenar_resultados, name='armazenar_resultados'),  # URL para armazenar resultados
    path('historico/', exibir_historico, name='historico'),  # URL para exibir histórico
    path('finalizar_teste/', finalizar_teste, name='finalizar_teste'),  # URL para finalizar teste
    path('perfil/', perfil, name='perfil'),  # URL para o perfil do usuário
    path('', home_view, name='home'),  # Página inicial
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



