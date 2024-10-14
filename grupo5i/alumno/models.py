from django.db import models

# Create your models here.

class Alumno(models.Model):
    apaterno=models.CharField(max_length=50,verbose_name="Apellido paterno jaja")
    amaterno=models.CharField(max_length=50,verbose_name="Apellido materno")
    nombre=models.CharField(max_length=100,verbose_name="Nombre(s)")
    fecha_nacimientp=models.DateField(max_length=100,verbose_name="fehca de nacimiento",null=False, blank=False)
    fecha_ingreso=models.DateField(verbose_name="Fecha de Ingreso", null=False, blank=False)