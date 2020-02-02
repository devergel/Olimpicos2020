from django.db import models


# Create your models here.
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=200)
    contrasena = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    Apellido = models.CharField(max_length=200)
    correo = models.CharField(max_length=1000)

    def __str__(self):
        return 'Usuario: ' + str(self.idUsuario)


class Evento(models.Model):
    idEvento = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=300)
    fecha = models.DateField(blank=True, auto_now=True)

    def __str__(self):
        return 'Id Evento: ' + str(self.idEvento) + ' --Mes-- ' + str(self.fecha.month)


class Deporte(models.Model):
    idDeporte = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return 'Deporte: ' + str(self.idDeporte)


class ModadalidadDeporte(models.Model):
    idModalidadDeporte = models.AutoField(primary_key=True)
    nombreModalidad = models.CharField(max_length=100)
    # id deporte apunta a deporte
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE, default='')

    def __str__(self):
        return 'Id ModalidadDeporte: ' + str(self.idModalidadDeporte)


class LugarNacimiento(models.Model):
    idLugarNacimiento = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return 'Id LugarNacimiento: ' + str(self.idLugarNacimiento)


class Delegacion(models.Model):
    idDelegacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    habilitado = models.BooleanField()

    def __str__(self):
        return 'Delegacion: ' + str(self.idDelegacion)


class Entrenador(models.Model):
    idEntrenador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return 'Entrenador: ' + str(self.idEntrenador)


class Deportista(models.Model):
    idDeportista = models.AutoField(primary_key=True)
    idEntrenador = models.ForeignKey(
        Entrenador, on_delete=models.CASCADE, default='')
    idDelegacion = models.ForeignKey(
        Delegacion, on_delete=models.CASCADE, default='')
    idLugarNacimiento = models.ForeignKey(
        LugarNacimiento, on_delete=models.CASCADE, default='')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    estatura = models.DecimalField(max_digits=6, decimal_places=2)
    foto = models.CharField(max_length=250)
    fechaNacimiento = models.DateField(blank=True, auto_now=True)
    # Tabla intermedia
    deportista = models.ManyToManyField(
        ModadalidadDeporte, through='DeportistaModalidad', default='')

    def __str__(self):
        return 'Deportista: ' + str(self.idDeportista)


class Participacion(models.Model):
    idParticipacion = models.AutoField(primary_key=True)
    usuarios = models.ManyToManyField(Usuario, through='Comentario')
    # id evento apunta a tabla Evento
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, default='')
    # id deportista apunta a tabla deportista
    deportista = models.ForeignKey(
        Deportista, on_delete=models.CASCADE, default='')
    # id modalidadDeporte tabla modalidadDeporte
    modalidadDeporte = models.ForeignKey(
        ModadalidadDeporte, on_delete=models.CASCADE, default='')
    linkVideo = models.CharField(max_length=300)

    def __str__(self):
        return 'Id Participacion: ' + str(self.idParticipacion)


class Comentario(models.Model):
    idComentario = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=300)
    # id usuario apunta a tabla Usuario
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default='')
    # id participacion apunta a tabla participacion
    participacion = models.ForeignKey(
        Participacion, on_delete=models.CASCADE, default='')
    fecha = models.DateField(blank=True, auto_now=True)

    def __str__(self):
        return 'Id Comentario: ' + str(self.idComentario)


class DeportistaModalidad(models.Model):
    idModalidadDeportista = models.AutoField(primary_key=True)
    # id deportista
    deportista = models.ForeignKey(
        Deportista, on_delete=models.CASCADE, default='')
    # id modalidad
    modalidad = models.ForeignKey(
        ModadalidadDeporte, on_delete=models.CASCADE, default='')

    def __str__(self):
        return 'Id ModalidadDeportista: ' + str(self.idModalidadDeportista)
