from django.db import models

class Iniciarseccion(models.Model):
    Email = models.EmailField()
    Password = models.TextField()


class contacto(models.Model):
    name = models.CharField(max_length=50)
    Email = models.EmailField()
    Message = models.TextField()






