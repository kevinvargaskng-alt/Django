from django.urls import path
from . import views

urlpatterns = [
    path('', views.intercentros_list, name='intercentros'),
    path('eliminar/<int:id>/', views.eliminar_torneo, name='eliminar_torneo_centro'),
    path('editar/<int:id>/', views.editar_torneo, name='editar_torneo_centro'),
]