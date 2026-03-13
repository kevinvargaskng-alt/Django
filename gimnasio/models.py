from django.db import models

class Entrenamiento(models.Model):
    codigo_entrenamiento = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    disciplina = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.disciplina} - {self.fecha}"

class Reserva(models.Model):
    codigo_registro = models.AutoField(primary_key=True)
    usuario_solicitante = models.CharField(max_length=100)
    hora_prestamo = models.TimeField()
    fecha_entrada = models.DateField()
    hora_entrada = models.TimeField()
    fecha_permanencia = models.DateField()
    hora_salida = models.TimeField()
    fecha_salida = models.DateField()
    entrenamiento = models.ForeignKey(
        Entrenamiento, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='reservas'
    )
    estado = models.CharField(max_length=20, default='Pendiente')

    def __str__(self):
        return f"{self.usuario_solicitante} - {self.fecha_entrada}"