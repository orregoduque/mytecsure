# Generated by Django 3.0.7 on 2022-11-18 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0015_evento_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='latitud',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='evento',
            name='longitud',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
