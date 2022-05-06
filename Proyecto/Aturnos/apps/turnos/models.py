from distutils.command.upload import upload
from pickle import TRUE
from pickletools import read_uint1
from unicodedata import name
from django.db import models
from datetime import datetime

# Create your models here.
class Usuarios(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    celular = models.CharField(max_length = 10)
    staff = models.CharField(max_length=2,null = True)
    foto = models.ImageField(upload_to = "images/",null = TRUE,blank = True)
    def __str__(self):
        return self.nombres
    def nombre(name):
        return name.nombres

class Turnos(models.Model):
    id = models.AutoField(primary_key = True)
    nturno = models.IntegerField()
    hora_creacion = models.DateTimeField(auto_now_add = True)
    estado = models.CharField(max_length = 10)
    usuario = models.SET(name)
    usuarioStaff = models.SET(name)