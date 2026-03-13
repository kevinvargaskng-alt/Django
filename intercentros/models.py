from django.db import models

class TorneoIntercentros(models.Model):
    codigo_torneo_centro = models.AutoField(primary_key=True)
    nombre_torneo = models.CharField(max_length=100)
    fecha_torneo = models.DateField()
    lugar = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, default='Activo')

    def __str__(self):
        return self.nombre_torneo

class EquipoIntercentros(models.Model):
    codigo_equipo_centro = models.AutoField(primary_key=True)
    nombre_equipo = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)
    torneo = models.ForeignKey(TorneoIntercentros, on_delete=models.CASCADE, related_name='equipos')

    def __str__(self):
        return self.nombre_equipo

class SeleccionadorSena(models.Model):
    codigo_seleccionador = models.AutoField(primary_key=True)
    nombre_seleccion = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=50)
    fecha_seleccion = models.DateField()

    def __str__(self):
        return self.nombre_seleccion

class ParticipacionIntercentros(models.Model):
    codigo_participacion = models.AutoField(primary_key=True)
    torneo = models.ForeignKey(TorneoIntercentros, on_delete=models.CASCADE)
    equipo = models.ForeignKey(EquipoIntercentros, on_delete=models.CASCADE)
    fecha_juego = models.DateField()
    puntaje = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.equipo} - {self.torneo}"