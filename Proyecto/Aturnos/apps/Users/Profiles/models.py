from distutils.command.upload import upload
from statistics import mode
from django.db import models
from pickle import TRUE


class Users(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    dni = models.CharField(max_length = 10)
    cell_phone_number = models.CharField(max_length = 10)
    staff = models.CharField(max_length=2,null = True)
    photo = models.ImageField(upload_to = "images/",null = TRUE,blank = True)
    def __str__(self):
        return self.name
