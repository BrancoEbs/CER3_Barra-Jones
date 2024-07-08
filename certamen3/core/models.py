from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = (
        ('operator', 'Operator'),
        ('supervisor', 'Supervisor'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLES)

class Planta(models.Model):
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=100)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class RegistroProduccion(models.Model):
    TURNOS = [
        ('AM', 'Mañana'),
        ('PM', 'Tarde'),
        ('MM', 'Noche'),
    ]
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    litros = models.FloatField()
    fecha_produccion = models.DateField()
    turno = models.CharField(max_length=2, choices=TURNOS)
    hora_registro = models.DateTimeField(auto_now_add=True)
    operador = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.producto.nombre} - {self.litros} litros'
