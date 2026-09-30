from django.db import models
from django.contrib.auth.models import User

class Viaje(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    destino = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.destino} ({self.fecha_inicio})"