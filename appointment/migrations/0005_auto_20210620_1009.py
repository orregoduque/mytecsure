# Generated by Django 3.0.7 on 2021-06-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='hospital_cercano',
            field=models.CharField(default='Imbanaco', max_length=300),
        ),
        migrations.AlterField(
            model_name='evento',
            name='actividad',
            field=models.CharField(default='interclases', max_length=300),
        ),
    ]
