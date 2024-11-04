from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ResultadosTeste, Dicas, HistoricoTeste
from .forms import CustomUserCreationForm, CustomUserChangeForm
from datetime import timedelta

# View para registro de usuário
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# View para edição de usuário
@login_required
def edit_user(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informações alteradas com sucesso!')
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'edit_user.html', {'form': form})

# View para login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Nome de usuário ou senha incorretos.")
    
    return render(request, 'login.html')

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
def salvar_resultados(request):
    if request.method == 'POST':
        frases = request.POST.getlist('frases')
        tempos = request.POST.getlist('tempos')
        erros_totais = sum(int(e) for e in request.POST.getlist('erros'))

        tempo_total = timedelta(seconds=sum(float(t) for t in tempos))
        palavras_total = sum(len(f.split()) for f in frases)
        palavras_por_minuto = (palavras_total / tempo_total.total_seconds()) * 60

        # Cria o registro no histórico do teste
        teste = HistoricoTeste.objects.create(
            usuario=request.user,
            erros=erros_totais,
            tempo_total=tempo_total,
            palavras_por_minuto=palavras_por_minuto
        )

        # Salva resultados de cada frase
        for frase, tempo, erros in zip(frases, tempos, request.POST.getlist('erros')):
            ResultadosTeste.objects.create(
                teste=teste,
                frase=frase,
                tempo_gasto=timedelta(seconds=float(tempo)),
                erros=int(erros)
            )

        return JsonResponse({'status': 'ok'})
    
    return JsonResponse({'status': 'erro'})

@login_required
def exibir_historico(request):
    historicos = HistoricoTeste.objects.filter(usuario=request.user)  # Obtenha registros do histórico do usuário
    return render(request, 'historico_testes.html', {'historicos': historicos})

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def teste_view(request):
    return render(request, 'teste.html')

@login_required
def dicas_view(request):
    dicas = Dicas.objects.all()
    return render(request, 'dicas.html', {'dicas': dicas})

@login_required
def finalizar_teste(request):
    if request.method == "POST":
        frases = request.POST.getlist('frases')
        erros_totais = sum(int(e) for e in request.POST.getlist('erros'))
        tempo_total = sum(float(t) for t in request.POST.getlist('tempos'))

        # Calcular a quantidade total de palavras
        palavras_total = sum(len(f.split()) for f in frases)
        palavras_por_minuto = (palavras_total / tempo_total) * 60

        # Criar o histórico do teste
        historico = HistoricoTeste.objects.create(
            usuario=request.user,
            erros=erros_totais,
            tempo_total=timedelta(seconds=tempo_total),
            palavras_por_minuto=palavras_por_minuto
        )

        # Salvar os resultados de cada frase
        for frase, tempo, erros in zip(frases, request.POST.getlist('tempos'), request.POST.getlist('erros')):
            ResultadosTeste.objects.create(
                teste=historico,
                frase=frase,
                tempo_gasto=timedelta(seconds=float(tempo)),
                erros=int(erros)
            )

        messages.success(request, "Teste finalizado com sucesso!")
        return redirect('historico')

    return render(request, 'finalizar_teste.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')

@login_required
def resultados_view(request):
    historico_testes = HistoricoTeste.objects.filter(usuario=request.user)
    return render(request, 'resultados.html', {'historico_testes': historico_testes})

# Adicione a função 'salvar_resultado_teste' como uma view (caso seja necessário)
@login_required
def salvar_resultado_teste(request):
    if request.method == 'POST':
        # Implementação da lógica para salvar resultados do teste
        # Isso é um espaço reservado; você deve implementar a lógica necessária.
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'erro'})
