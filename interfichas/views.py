from django.shortcuts import render, redirect, get_object_or_404
from .models import TorneoInterfichas, EquipoInterfichas

# LISTAR Y CREAR
def interfichas_list(request):
    torneos = TorneoInterfichas.objects.all()
    if request.method == 'POST':
        TorneoInterfichas.objects.create(
            nombre_torneo=request.POST.get('nombre'),
            fecha_torneo_fichas=request.POST.get('fecha'),
            horario_torneo_fichas=request.POST.get('hora'),
            lugar=request.POST.get('lugar'),
            disciplina=request.POST.get('disciplina')
        )
        return redirect('interfichas')
    
    return render(request, 'interfichas/interfichas.html', {'torneos': torneos})

# ELIMINAR
def eliminar_torneo(request, id):
    torneo = get_object_or_404(TorneoInterfichas, codigo_torneo_fichas=id)
    torneo.delete()
    return redirect('interfichas')

# EDITAR
def editar_torneo(request, id):
    torneo = get_object_or_404(TorneoInterfichas, codigo_torneo_fichas=id)
    if request.method == 'POST':
        torneo.nombre_torneo = request.POST.get('nombre')
        torneo.disciplina = request.POST.get('disciplina')
        torneo.save()
        return redirect('interfichas')
    return render(request, 'interfichas/editar.html', {'torneo': torneo})