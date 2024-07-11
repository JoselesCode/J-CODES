from django.db import models

class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30,null = False)
    apellido = models.CharField(max_length=30,null = False)
    correo = models.CharField(max_length=50,null = False)
    telefono =models.IntegerField(null=False)
    f_nac  = models.DateField(null=True)
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
class Productos(models.Model):
    id2 = models.IntegerField(primary_key=True)
    nombre2 = models.CharField(max_length=30,null = False)
    precio2 =models.IntegerField(null=False)
    f_registro2 = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'usuarios'
        db_table = 'productos'