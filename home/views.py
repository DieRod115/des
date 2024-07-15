from django.shortcuts import render, get_object_or_404
from .models import Project
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

def games(request):
    return render(request, 'home/games.html')

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'home/project_list.html', {'projects': projects})

def games_list(request):
    games = Project.objects.all()
    return render(request, 'home/games_list.html', {'games': games})

def comprar_juego(request, game_id):
    game = get_object_or_404(Project, pk=game_id)
    # Aquí puedes implementar la lógica para realizar la compra
    return HttpResponse(f"Ruta agregada: {game.title}")

def agregar_al_carrito(request, game_id):
    game = get_object_or_404(Project, pk=game_id)
    # Aquí puedes implementar la lógica para agregar al carrito
    return HttpResponse(f"Has añadido al carrito el juego: {game.title}")

@csrf_exempt
def csrf_failure(request, reason=""):
    return render(request, '403.html', status=403)

# Create your views here.
def base(request):
    return render(request, "home/base.html")
def home(request):
    return render(request, "home/home.html")
def about(request):
    return render(request, "home/about.html")
def regencomienda(request):
    return render(request, "home/regencomienda.php")
def pagos(request):
    return render(request, "home/pagos.html")
def datos(request):
    return render(request, "home/datos.php")
def encomiendas(request):
    return render(request, "home/encomiendas.php")
                  
