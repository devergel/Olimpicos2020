# Generated by Django 2.1 on 2020-02-16 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0009_merge_20200215_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='participacion',
            name='resultado',
            field=models.CharField(max_length=300, null=True),
        ),
    ]