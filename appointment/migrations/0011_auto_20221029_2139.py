# Generated by Django 3.0.7 on 2022-10-29 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0010_auto_20221029_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='lugar',
            field=models.CharField(choices=[('Parque', 'Parque'), ('Colegio', 'Americano'), ('Universidad', 'Frances'), ('Rural', 'Bolivar'), ('Barrio', 'Finca'), ('Campo Deportivo', 'Campo Deportivo')], default='Parque', max_length=16),
        ),
    ]
