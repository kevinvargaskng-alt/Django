from django.shortcuts import render, redirect, get_object_or_404
from .models import TorneoIntercentros, EquipoIntercentros

# LISTAR Y CREAR
def intercentros_list(request):
    torneos = TorneoIntercentros.objects.all()
    if request.method == 'POST':
        TorneoIntercentros.objects.create(
            nombre_torneo=request.POST.get('nombre'),
            fecha_torneo=request.POST.get('fecha'),
            lugar=request.POST.get('lugar'),
            disciplina=request.POST.get('disciplina')
        )
        return redirect('intercentros')
    return render(request, 'intercentros/intercentros.html', {'torneos': torneos})

# ELIMINAR
def eliminar_torneo(request, id):
    torneo = get_object_or_404(TorneoIntercentros, codigo_torneo_centro=id)
    torneo.delete()
    return redirect('intercentros')

# EDITAR
def editar_torneo(request, id):
    torneo = get_object_or_404(TorneoIntercentros, codigo_torneo_centro=id)
    if request.method == 'POST':
        torneo.nombre_torneo = request.POST.get('nombre')
        torneo.disciplina = request.POST.get('disciplina')
        torneo.lugar = request.POST.get('lugar')
        torneo.save()
        return redirect('intercentros')
    return render(request, 'intercentros/editar.html', {'torneo': torneo})