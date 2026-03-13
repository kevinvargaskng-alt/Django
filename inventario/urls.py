from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventario_list, name='inventario'),
    path('eliminar-elemento/<int:id>/', views.eliminar_elemento, name='eliminar_elemento'),
    path('editar-elemento/<int:id>/', views.editar_elemento, name='editar_elemento'),
    path('eliminar-prestamo/<int:id>/', views.eliminar_prestamo, name='eliminar_prestamo'),
]