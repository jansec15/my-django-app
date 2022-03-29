from pyexpat import model
from django.db import models

# Create your models here.

# Clase para generar desplegable en la clase pacientes, tipo de identidad
class TipoIdentificacion(models.Model):
    acronimo=models.CharField(max_length=4)
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.acronimo

# Cliente en la admision
class Paciente(models.Model):
    # Selector de sexo
    class sexyEnum(models.TextChoices):
        MASCULINO = 'Masculino'
        FEMENINO = 'Femenino'
    # Selector de tipo de sangre
    class bloodEnum(models.TextChoices):
        NONE=''
        A1 = 'A+'
        A2 = 'A-'
        B1 = 'B+'
        B2 = 'B-'
        AB1 = 'AB+'
        AB2 = 'AB-'
        O1 = 'O+'
        O2 = 'O-'

    tipo_idenfiticacion=models.ForeignKey('TipoIdentificacion',on_delete=models.DO_NOTHING, null=True,blank=True)
    numero_identificacion=models.CharField(max_length=30)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100, null=True,blank=True)
    sexo=models.CharField(max_length=9,choices=sexyEnum.choices,default=sexyEnum.MASCULINO)
    fecha_nacimiento=models.CharField(max_length=10,default='1/1/2000')
    telefono=models.CharField(max_length=20, null=True,blank=True)
    email=models.EmailField(max_length=200, null=True,blank=True)
    pais_nacimiento=models.CharField(max_length=20, null=True,blank=True)
    pais_residencia=models.CharField(max_length=20,null=True,blank=True)
    direccion=models.CharField(max_length=100,null=True,blank=True)
    ocupacion=models.CharField(max_length=20,null=True,blank=True)
    tipo_sangre=models.CharField(max_length=10,choices=bloodEnum.choices,default=bloodEnum.NONE)
    create=models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numero_identificacion + ' - ' + self.nombre + ' ' + self.apellido




    