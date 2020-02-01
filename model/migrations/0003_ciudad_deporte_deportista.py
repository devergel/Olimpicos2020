# Generated by Django 3.0.2 on 2020-02-01 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_delegacion_entrenador_pais'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('idCiudad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('idPais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('idDeporte', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Deportista',
            fields=[
                ('idDeportista', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=6)),
                ('estatura', models.DecimalField(decimal_places=2, max_digits=6)),
                ('foto', models.CharField(max_length=250)),
                ('idCiudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.Ciudad')),
                ('idDelegacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.Delegacion')),
                ('idEntrenador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.Entrenador')),
            ],
        ),
    ]