from django.urls import path
from . import views

urlpatterns = [
    path('', views.interfichas_list, name='interfichas'),
    path('eliminar/<int:id>/', views.eliminar_torneo, name='eliminar_torneo'),
    path('editar/<int:id>/', views.editar_torneo, name='editar_torneo'),
    path('crear-equipo/', views.crear_equipo, name='crear_equipo'),
    path('', views.lista_torneos, name='lista_torneos'),           # Página principal
    path('crear-equipo/', views.crear_equipo, name='crear_equipo'), # URL para guardar equipo
]