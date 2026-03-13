from django.urls import path
from . import views

urlpatterns = [
    path('', views.interfichas_list, name='interfichas'),
    path('eliminar/<int:id>/', views.eliminar_torneo, name='eliminar_torneo'),
    path('editar/<int:id>/', views.editar_torneo, name='editar_torneo'),
]