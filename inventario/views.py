from django.shortcuts import render, redirect, get_object_or_404
from .models import ElementoDeportivo, Prestamo, Devolucion, Sancion, Revision

def inventario_list(request):
    elementos = ElementoDeportivo.objects.all()
    prestamos = Prestamo.objects.all().order_by('-fecha_prestamo')
    sanciones = Sancion.objects.all()

    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'crear_elemento':
            ElementoDeportivo.objects.create(
                tipo_maquina=request.POST.get('tipo_maquina'),
                cantidad_total=request.POST.get('cantidad_total'),
                estado_general=request.POST.get('estado_general'),
                fecha_adquisicion=request.POST.get('fecha_adquisicion'),
                descripcion=request.POST.get('descripcion'),
                docente_responsable=request.POST.get('docente_responsable'),
            )
            return redirect('inventario')

        if accion == 'crear_prestamo':
            Prestamo.objects.create(
                elemento_id=request.POST.get('elemento'),
                hora_prestamo=request.POST.get('hora_prestamo'),
                dias_prestamo=request.POST.get('dias_prestamo'),
                fecha_devolucion=request.POST.get('fecha_devolucion'),
                cantidad_prestada=request.POST.get('cantidad_prestada'),
                observacion_prestamo=request.POST.get('observacion'),
            )
            return redirect('inventario')

    return render(request, 'inventario/inventario.html', {
        'elementos': elementos,
        'prestamos': prestamos,
        'sanciones': sanciones,
    })

def eliminar_elemento(request, id):
    elemento = get_object_or_404(ElementoDeportivo, codigo_elemento=id)
    elemento.delete()
    return redirect('inventario')

def editar_elemento(request, id):
    elemento = get_object_or_404(ElementoDeportivo, codigo_elemento=id)
    if request.method == 'POST':
        elemento.tipo_maquina = request.POST.get('tipo_maquina')
        elemento.cantidad_total = request.POST.get('cantidad_total')
        elemento.estado_general = request.POST.get('estado_general')
        elemento.docente_responsable = request.POST.get('docente_responsable')
        elemento.save()
        return redirect('inventario')
    return render(request, 'inventario/editar.html', {'elemento': elemento})

def eliminar_prestamo(request, id):
    prestamo = get_object_or_404(Prestamo, codigo_prestamo=id)
    prestamo.delete()
    return redirect('inventario')