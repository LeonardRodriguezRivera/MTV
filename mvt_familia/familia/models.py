from django.db import models


# Create your models here.

class Familia(models.Model):
    name = models.CharField(max_length=40)
    edad = models.CharField(max_length=40)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    email = models.EmailField()