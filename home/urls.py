from django.urls import path
from . import views

urlpatterns = [
    path('proyectos/', views.games, name='games'),
    path('proyectos/', views.project_list, name='project_list'),
    path('juegos/', views.games_list, name='games_list'),
    path('juegos/comprar/<int:game_id>/', views.comprar_juego, name='comprar_juego'),
    path('juegos/agregar-al-carrito/<int:game_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
]
