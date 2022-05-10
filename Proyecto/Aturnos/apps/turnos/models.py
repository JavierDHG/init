from distutils.command.upload import upload
from pickle import TRUE
from unicodedata import name
from django.db import models
from datetime import datetime

# Create your models here.
class Turns(models.Model):
    id = models.AutoField(primary_key = True)
    turns = models.IntegerField()
    time = models.DateTimeField(auto_now_add = True)
    state = models.CharField(max_length = 10)
    user = models.CharField(max_length = 20)
    Staff = models.CharField(max_length = 20)