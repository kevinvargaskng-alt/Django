from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

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
    
    
class Equipo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Equipo")
    tag = models.CharField(max_length=10, unique=True, verbose_name="Tag")
    capitan = models.CharField(max_length=80, blank=True, null=True, verbose_name="Capitán")
    
    disciplina = models.CharField(max_length=50, verbose_name="Disciplina")
    
    jugadores = models.TextField(blank=True, null=True, verbose_name="Jugadores")
    
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="equipos_creados"
    )

    def __str__(self):
        return f"{self.nombre} ({self.tag})"

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ['-fecha_inscripcion']
