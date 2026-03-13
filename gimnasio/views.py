from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva, Entrenamiento

# LISTAR Y CREAR RESERVAS
def gimnasio_list(request):
    reservas = Reserva.objects.all().order_by('-fecha_entrada')
    entrenamientos = Entrenamiento.objects.all()

    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'crear_reserva':
            Reserva.objects.create(
                usuario_solicitante=request.POST.get('usuario'),
                hora_prestamo=request.POST.get('hora_prestamo'),
                fecha_entrada=request.POST.get('fecha_entrada'),
                hora_entrada=request.POST.get('hora_entrada'),
                fecha_permanencia=request.POST.get('fecha_permanencia'),
                hora_salida=request.POST.get('hora_salida'),
                fecha_salida=request.POST.get('fecha_salida'),
            )
            return redirect('gimnasio')

        if accion == 'crear_entrenamiento':
            Entrenamiento.objects.create(
                fecha=request.POST.get('fecha'),
                hora=request.POST.get('hora'),
                disciplina=request.POST.get('disciplina'),
            )
            return redirect('gimnasio')

    return render(request, 'gimnasio/gimnasio.html', {
        'reservas': reservas,
        'entrenamientos': entrenamientos,
    })

# ELIMINAR RESERVA
def eliminar_reserva(request, id):
    reserva = get_object_or_404(Reserva, codigo_registro=id)
    reserva.delete()
    return redirect('gimnasio')

# EDITAR RESERVA
def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, codigo_registro=id)
    if request.method == 'POST':
        reserva.usuario_solicitante = request.POST.get('usuario')
        reserva.fecha_entrada = request.POST.get('fecha_entrada')
        reserva.hora_entrada = request.POST.get('hora_entrada')
        reserva.hora_salida = request.POST.get('hora_salida')
        reserva.fecha_salida = request.POST.get('fecha_salida')
        reserva.save()
        return redirect('gimnasio')
    return render(request, 'gimnasio/editar.html', {'reserva': reserva})

# ELIMINAR ENTRENAMIENTO
def eliminar_entrenamiento(request, id):
    entrenamiento = get_object_or_404(Entrenamiento, codigo_entrenamiento=id)
    entrenamiento.delete()
    return redirect('gimnasio')