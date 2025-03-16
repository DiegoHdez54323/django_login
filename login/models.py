from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de usuario")
    correo = models.EmailField(unique=True, verbose_name="Correo electrónico")
    contraseña = models.CharField(max_length=128, verbose_name="Contraseña")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

