from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Evento(models.Model):
    idEvento = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=300)
    fecha = models.DateField(blank=True, auto_now=True)

    def __str__(self):
        return 'Id Evento: ' + str(self.idEvento) + ' --Mes-- ' + str(self.fecha.month)


class LugarNacimiento(models.Model):
    idLugarNacimiento = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return 'LugarNacimiento: ' + str(self.pais + " - " + self.ciudad)


class Delegacion(models.Model):
    idDelegacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    habilitado = models.BooleanField()

    def __str__(self):
        return 'Delegacion: ' + str(self.nombre + " -- Habilitado :" + str(self.habilitado))


class Entrenador(models.Model):
    idEntrenador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return 'Entrenador: ' + str(self.nombre + "" + self.apellido)


class Deporte(models.Model):
    idDeporte = models.AutoField(primary_key=True)
    nombreDeporte = models.CharField(max_length=100)
    icono = models.ImageField(upload_to='model/static/images', null=True)

    def __str__(self):
        return 'Deporte: ' + str(self.nombreDeporte)


class ModadalidadDeporte(models.Model):
    idModalidadDeporte = models.AutoField(primary_key=True)
    nombreModalidad = models.CharField(max_length=100)
    # id del deporte al que pertenece la modalidad
    idDeporte = models.ForeignKey(
        Deporte, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return 'ModalidadDeporte: ' + str(self.nombreModalidad)


class Deportista(models.Model):
    idDeportista = models.AutoField(primary_key=True)
    idEntrenador = models.ForeignKey(
        Entrenador, on_delete=models.CASCADE,  blank=True, null=True)
    idDelegacion = models.ForeignKey(
        Delegacion, on_delete=models.CASCADE,  blank=True, null=True)
    idLugarNacimiento = models.ForeignKey(
        LugarNacimiento, on_delete=models.CASCADE,  blank=True, null=True)
    idModalidadDeporte = models.ForeignKey(
        ModadalidadDeporte, on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    estatura = models.DecimalField(max_digits=6, decimal_places=2)
    foto = models.CharField(max_length=250)
    fechaNacimiento = models.DateField(blank=True, auto_now=True)

    def __str__(self):
        return 'Deportista: ' + str(self.nombre + " " + self.apellido)


class Participacion(models.Model):
    idParticipacion = models.AutoField(primary_key=True)
    #usuarios = models.ManyToManyField(Usuario, through='Comentario')
    # id evento apunta a tabla Evento
    evento = models.ForeignKey(
        Evento, on_delete=models.CASCADE,  blank=True, null=True)
    # id deportista apunta a tabla deportista
    deportista = models.ForeignKey(
        Deportista, on_delete=models.CASCADE, default='')
    # id modalidadDeporte tabla modalidadDeporte
    modalidadDeporte = models.ForeignKey(
        ModadalidadDeporte, on_delete=models.CASCADE,  blank=True, null=True)
    linkVideo = models.CharField(max_length=300)
    resultado = models.CharField(max_length=300, null=True)

    def __str__(self):
        return 'Id Participacion: ' + str(self.idParticipacion)


class Comentario(models.Model):
    idComentario = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=300)
    # id usuario apunta a tabla Usuario
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE,  blank=True, null=True)
    # id participacion apunta a tabla participacion
    participacion = models.ForeignKey(
        Participacion, on_delete=models.CASCADE,  blank=True, null=True)
    fecha = models.DateField(blank=True, auto_now=True)

    def __str__(self):
        return 'Id Comentario: ' + str(self.idComentario)
