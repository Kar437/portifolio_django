from django.shortcuts import render


# Create your views here.
def index (request):
    return render (request, "pag_principal/index.html")

def sobre (request):
    return render (request, "sobre/sobre.html")

def todos (request):
    return render (request, "projetos/todos.html")


# views das páginas dos projetos

def invasão_espacial (request):
    return render (request, "projetos/invasão_espacial.html")

def site_portfolio (request):
    return render (request, "projetos/site_portfolio.html")

def bot_automacao (request):
    return render (request, "projetos/bot_automacao.html")

def mearm (request):
    return render (request, "projetos/mearm.html")