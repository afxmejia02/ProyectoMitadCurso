from django.db import models

# Create your models here.



class TipoDocumento(models.Model):
    Id = models.AutoField(primary_key=True)
    TIPOS_DOCUMENTO = [
    ('RC', 'REGISTRO CIVIL DE NACIMIENTO'),
    ('TI', 'TARJETA DE IDENTIDAD'),
    ('CC', 'CEDULA DE CIUDADANIA'),
    ('TE', 'TARJETA DE EXTRANJERIA'),
    ('CE', 'CEDULA DE EXTRANJERIA'),
    ('NIT', 'NIT'),
    ('PAS', 'PASAPORTE'),
]
    Nombre = models.CharField(max_length=100, choices=TIPOS_DOCUMENTO, unique=True)
    Descripcion = models.CharField(max_length=500)

    def __str__(self):return  self.get_Nombre_display()


class Ciudad(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, unique=True)
    Descripcion = models.CharField(max_length=500) 

    def __str__(self):return self.Nombre

class Persona(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    IdTipoDocumento = models.ForeignKey(TipoDocumento, null=False, blank=False, on_delete=models.CASCADE)
    Documento = models.CharField(max_length=50)
    LugarResidencia = models.ForeignKey(Ciudad, null=False, blank=False, on_delete=models.CASCADE)
    FechaNacimiento = models.DateField()
    Email = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=50)
    Usuario = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=100)

    def __str__(self):return self.Nombres  + " " + self.Apellidos
    