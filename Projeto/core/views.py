from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
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
            return redirect('home')
    return render(request, 'login.html')

@login_required
def teste_view(request):
    if request.method == "POST":
        try:
            acertos = int(request.POST.get('acertos', 0))
            erros = int(request.POST.get('erros', 0))

            ResultadosTeste.objects.create(usuario=request.user, acertos=acertos, erros=erros)
            return redirect('home')  # Redirecionar após salvar os resultados
        except ValueError:
            # Adicione uma mensagem de erro caso a conversão falhe
            return render(request, 'teste.html', {'error': 'Valores inválidos para acertos ou erros.'})

    return render(request, 'teste.html')

def dicas_view(request):
    dicas = Dicas.objects.all()
    return render(request, 'dicas.html', {'dicas': dicas})

@login_required
def armazenar_resultados(request):
    if request.method == 'POST':
        usuario = request.user
        texto = request.POST.get('texto')
        tempo = request.POST.get('tempo')
        erros = request.POST.get('erros')

        # Verifique se os dados necessários foram fornecidos
        if texto and tempo and erros is not None:
            HistoricoTeste.objects.create(
                usuario=usuario,
                texto=texto,
                tempo=tempo,
                erros=int(erros)  # Garanta que os erros sejam armazenados como inteiro
            )
            return redirect('perfil')
        else:
            # Adicione uma mensagem de erro caso os campos estejam vazios
            return render(request, 'perfil.html', {'error': 'Por favor, preencha todos os campos.'})

@login_required
def exibir_historico(request):
    usuario = request.user
    historico = HistoricoTeste.objects.filter(usuario=usuario)

    filtro = request.GET.get('filtro', 'recentes')

    if filtro == 'menos_erros':
        historico = historico.order_by('erros')
    elif filtro == 'melhor_tempo':
        historico = historico.order_by('tempo')
    else:  # Recentes
        historico = historico.order_by('-data_realizacao')

    return render(request, 'perfil.html', {'historico': historico})

@login_required
def finalizar_teste(request):
    if request.method == "POST":
        texto = request.POST.get("texto")
        tempo = request.POST.get("tempo")
        erros = request.POST.get("erros")

        # Verifique se os dados necessários foram fornecidos
        if texto and tempo and erros is not None:
            HistoricoTeste.objects.create(
                usuario=request.user,
                texto=texto,
                erros=int(erros),  # Garanta que os erros sejam armazenados como inteiro
                tempo=tempo
            )
            return redirect('pagina_de_sucesso')
        else:
            # Adicione uma mensagem de erro caso os campos estejam vazios
            return render(request, 'finalizar_teste.html', {'error': 'Por favor, preencha todos os campos.'})

@login_required
def perfil(request):
    historico = HistoricoTeste.objects.filter(usuario=request.user).order_by('-data_realizacao')
    return render(request, 'perfil.html', {'historico': historico})
