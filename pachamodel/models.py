from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    riego = models.CharField(max_length=200, default=0)
    solhoras = models.CharField(max_length=200, default=0)
    expresion = models.CharField(max_length=200, default=0)
    tempExt = models.CharField(max_length=200, default=0)
    humInt = models.CharField(max_length=200, default=0)
    humExt = models.CharField(max_length=200, default=0)
    luzUV = models.CharField(max_length=200, default=0)
    luz = models.CharField(max_length=200, default=0)
    nivel = models.CharField(max_length=200, default=0)
    modo = models.CharField(max_length=200, default=0)
    
    def __str__(self):
        return self.usuario