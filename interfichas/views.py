from django.shortcuts import render, redirect, get_object_or_404
from .models import TorneoInterfichas, EquipoInterfichas
from django.http import JsonResponse
from .models import Equipo


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


# crear equipo
def lista_torneos(request):
    """Página principal donde aparece el botón para inscribir equipo"""
    return render(request, 'interfichas.html')   # Cambia el nombre si tu template se llama diferente

def crear_equipo(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre', '').strip()
            tag = request.POST.get('tag', '').strip().upper()
            capitan = request.POST.get('capitan', '').strip()
            disciplina = request.POST.get('disciplina', '').strip()
            jugadores_lista = request.POST.getlist('jugadores[]')   # Recibe los jugadores

            # Validaciones básicas
            if not nombre or not tag or not disciplina:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Nombre, Tag y Disciplina son obligatorios'
                }, status=400)

            # Convertir lista de jugadores a texto separado por comas
            jugadores_texto = ", ".join(jugadores_lista) if jugadores_lista else ""

            # Crear y guardar el equipo
            equipo = Equipo(
                nombre=nombre,
                tag=tag,
                capitan=capitan,
                disciplina=disciplina,
                jugadores=jugadores_texto
            )

            if request.user.is_authenticated:
                equipo.creado_por = request.user

            equipo.save()

            return JsonResponse({
                'status': 'success',
                'message': f'¡Equipo "{nombre}" ({tag}) inscrito correctamente!'
            })

        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': 'Error al guardar el equipo'
            }, status=500)

    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)