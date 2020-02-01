from django.db import models


# Create your models here.
class User(models.Model):
    idUser = models.AutoField(primary_key=True)
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=1000)

    def __str__(self):
        return 'User: ' + self.idUser


class Pais(models.Model):
    idPais = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return 'Pais: ' + self.idPais

class Delegacion(models.Model):
    idDelegacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    habilitado = models.BooleanField()

    def __str__(self):
        return 'Delegacion: ' + self.idDelegacion


class Entrenador(models.Model):
    idEntrenador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return 'Entrenador: ' + self.idEntrenador
