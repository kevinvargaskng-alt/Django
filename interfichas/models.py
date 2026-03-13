from django.db import models

class TorneoInterfichas(models.Model):
    codigo_torneo_fichas = models.AutoField(primary_key=True)
    nombre_torneo = models.CharField(max_length=100)
    fecha_torneo_fichas = models.DateField()
    horario_torneo_fichas = models.TimeField()
    lugar = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, default='Activo')

    def __str__(self):
        return self.nombre_torneo

class EquipoInterfichas(models.Model):
    codigo_equipo_interfichas = models.AutoField(primary_key=True)
    ficha = models.IntegerField()
    nombre_equipo = models.CharField(max_length=100)
    fecha_creacion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='Inscrito')
    disciplina = models.CharField(max_length=50)
    torneo = models.ForeignKey(TorneoInterfichas, on_delete=models.CASCADE, related_name='equipos')

    def __str__(self):
        return f"{self.nombre_equipo} ({self.ficha})"