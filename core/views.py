from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ResultadosTeste, Dicas, HistoricoTeste

@login_required
def salvar_resultados(request):
    if request.method == 'POST':
        dados = request.POST
        frases = dados.get('frases')
        tempo_total = dados.get('tempo')
        erros_total = int(dados.get('erros'))

        HistoricoTeste.objects.create(
            usuario=request.user,
            frases=frases,
            tempo_total=tempo_total,
            erros_total=erros_total
        )
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'erro'})

def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        senha = request.POST['senha']
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('teste')
        else:
            messages.error(request, 'Email ou senha incorretos.')
    return render(request, 'login.html')

@login_required
def editar_login_view(request):
    if request.method == "POST":
        novo_email = request.POST['email']
        nova_senha = request.POST['senha']
        senha_antiga = request.POST['senha_antiga']

        user = authenticate(request, username=request.user.username, password=senha_antiga)

        if user is not None:
            if novo_email:
                user.email = novo_email
            if nova_senha:
                user.set_password(nova_senha)
                update_session_auth_hash(request, user)

            user.save()
            messages.success(request, 'Seu login foi atualizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Senha antiga incorreta. Por favor, tente novamente.')

    return render(request, 'editar_login.html')

@login_required
def excluir_login_view(request):
    if request.method == "POST":
        senha = request.POST.get('senha')
        user = authenticate(username=request.user.username, password=senha)

        if user is not None:
            user.delete()
            messages.success(request, "Sua conta foi excluída com sucesso.")
            return redirect('home')
        else:
            messages.error(request, "Senha incorreta. Não foi possível excluir sua conta.")
    
    return render(request, 'excluir_login.html')

@login_required
def teste_view(request):
    return render(request, 'teste.html')

@login_required
def dicas_view(request):
    dicas = Dicas.objects.all()
    return render(request, 'dicas.html', {'dicas': dicas})

@login_required
def armazenar_resultados(request):
    if request.method == "POST":
        erros = request.POST.get('erros')
        tempo = request.POST.get('tempo')
        texto = request.POST.get('texto')

        resultado = ResultadosTeste(usuario=request.user, erros=erros, tempo=tempo)
        resultado.save()

        historico = HistoricoTeste(usuario=request.user, frases=texto, erros_total=erros, tempo_total=tempo)
        historico.save()

        messages.success(request, "Resultados armazenados com sucesso!")
        return redirect('historico')

    return render(request, 'teste.html')

@login_required
def exibir_historico(request):
    historico = HistoricoTeste.objects.filter(usuario=request.user)
    return render(request, 'historico.html', {'historico': historico})

@login_required
def finalizar_teste(request):
    if request.method == "POST":
        erros = request.POST.get('erros')
        tempo = request.POST.get('tempo')
        texto = request.POST.get('texto')

        resultado = ResultadosTeste(usuario=request.user, erros=erros, tempo=tempo)
        resultado.save()

        historico = HistoricoTeste(usuario=request.user, frases=texto, erros_total=erros, tempo_total=tempo)
        historico.save()

        messages.success(request, "Teste finalizado com sucesso!")
        return redirect('historico')

    return render(request, 'finalizar_teste.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')

@login_required
def resultados_view(request):
    historico_testes = HistoricoTeste.objects.filter(usuario=request.user)
    return render(request, 'resultados.html', {
        'historico_testes': historico_testes,
    })
