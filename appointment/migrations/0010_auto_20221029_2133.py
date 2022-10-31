# Generated by Django 3.0.7 on 2022-10-29 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0009_remove_evento_director'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='hospital_cercano',
        ),
        migrations.AddField(
            model_name='evento',
            name='ciudad',
            field=models.CharField(choices=[('Cali', 'Cali'), ('Bogota', 'Bogota'), ('Medellin', 'Medellin'), ('Barranquilla ', 'Barranquilla ')], default='Cali', max_length=13),
        ),
    ]
