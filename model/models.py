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