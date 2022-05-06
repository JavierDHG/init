from distutils.command.upload import upload
from pickle import TRUE
from pickletools import read_uint1
from django.db import models

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