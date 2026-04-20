from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date
from .models import TorneoIntercentros, EquipoIntercentros

@login_required
def intercentros_list(request):
    # Traemos las convocatorias de torneos (Intercentros)
    torneos = TorneoIntercentros.objects.all().order_by('-fecha_torneo')
    
    # Traemos las postulaciones del usuario logueado (Opcional si tienes el modelo)
    # mis_postulaciones = EquipoIntercentros.objects.filter(numero_documento=request.user.numero_documento)

    if request.method == 'POST':
        accion = request.POST.get('accion')

        # 1. ACCIÓN: El aprendiz se postula automáticamente
        if accion == 'inscribir_aprendiz':
            disciplina = request.POST.get('disciplina')
            
            # Aquí guardarías en tu modelo de EquipoIntercentros
            # EquipoIntercentros.objects.create(
            #     nombres=request.user.first_name,
            #     apellidos=request.user.last_name,
            #     documento=request.user.numero_documento,
            #     ficha=request.user.ficha,
            #     programa=request.user.programa_formacion,
            #     disciplina=disciplina
            # )
            
            messages.success(request, f"¡Postulación para {disciplina} enviada exitosamente!")
            return redirect('intercentros')

        # 2. ACCIÓN: Crear torneo (Uso administrativo)
        elif accion == 'crear_torneo':
            # Validar y sanitizar datos de entrada
            nombre = request.POST.get('nombre', '').strip()
            fecha_str = request.POST.get('fecha', '').strip()
            lugar = request.POST.get('lugar', '').strip()
            disciplina_id = request.POST.get('disciplina', '').strip()
            
            # Validar que los campos requeridos no estén vacíos
            if not nombre or not fecha_str or not lugar or not disciplina_id:
                messages.error(request, "Por favor, completa todos los campos requeridos.")
                return redirect('intercentros')
            
            # Validar longitud del nombre
            if len(nombre) > 100:
                messages.error(request, "El nombre del torneo no puede exceder 100 caracteres.")
                return redirect('intercentros')
            
            # Validar formato de fecha
            try:
                fecha = timezone.datetime.strptime(fecha_str, '%Y-%m-%d').date()
                if fecha < date.today():
                    messages.error(request, "La fecha del torneo debe ser igual o posterior a hoy.")
                    return redirect('intercentros')
            except (ValueError, TypeError):
                messages.error(request, "Formato de fecha inválido. Usa YYYY-MM-DD.")
                return redirect('intercentros')
            
            # Validar que la disciplina exista
            from .models import Disciplina
            try:
                disciplina = Disciplina.objects.get(pk=disciplina_id)
            except Disciplina.DoesNotExist:
                messages.error(request, "La disciplina seleccionada no existe.")
                return redirect('intercentros')
            
            # Crear torneo con datos validados
            TorneoIntercentros.objects.create(
                nombre_torneo=nombre,
                fecha_torneo=fecha,
                lugar=lugar,
                disciplina=disciplina
            )
            messages.success(request, "Nueva convocatoria Intercentros publicada.")
            return redirect('intercentros')

    return render(request, 'intercentros/intercentros.html', {
        'torneos': torneos,
        'ahora': timezone.localtime(timezone.now()),
    })

@login_required
def eliminar_torneo(request, id):
    torneo = get_object_or_404(TorneoIntercentros, codigo_torneo_centro=id)
    torneo.delete()
    messages.warning(request, "Convocatoria eliminada correctamente.")
    return redirect('intercentros')