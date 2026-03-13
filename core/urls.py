from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Inicio
    path('', include('inicio.urls')),  # esto usa name='home' en inicio/urls.py
    path('interfichas/', include('interfichas.urls')),
    path('intercentros/', include('intercentros.urls')),
    path('gimnasio/', include('gimnasio.urls')),
    path('inventario/', include('inventario.urls')),
]