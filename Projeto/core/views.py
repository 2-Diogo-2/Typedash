from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ResultadosTeste, Dicas, HistoricoTeste

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
        email = request.POST['email']
        senha = request.POST['senha']
        senha_antiga = request.POST.get('senha_antiga')

        user = authenticate(request, username=request.user.username, password=senha_antiga)

        if user is not None:
            user.email = email
            user.set_password(senha)
            user.save()

            messages.success(request, 'Seu login foi atualizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Senha antiga incorreta.')

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

        resultado = ResultadosTeste(user=request.user, erros=erros, tempo=tempo)
        resultado.save()

        messages.success(request, "Resultados armazenados com sucesso!")
        return redirect('historico')

    return render(request, 'teste.html')

@login_required
def exibir_historico(request):
    historico = HistoricoTeste.objects.filter(user=request.user)
    return render(request, 'historico.html', {'historico': historico})

@login_required
def finalizar_teste(request):
    if request.method == "POST":
        # Implementar lógica para finalizar e armazenar os resultados
        erros = request.POST.get('erros')
        tempo = request.POST.get('tempo')
        resultado = ResultadosTeste(user=request.user, erros=erros, tempo=tempo)
        resultado.save()

        messages.success(request, "Teste finalizado com sucesso!")
        return redirect('historico')

    return render(request, 'finalizar_teste.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')
