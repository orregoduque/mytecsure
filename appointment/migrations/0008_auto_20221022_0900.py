# Generated by Django 3.0.7 on 2022-10-22 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_auto_20221021_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='lugar',
            field=models.CharField(choices=[('Colombo', 'Colombo'), ('Americano', 'Americano'), ('Frances', 'Frances'), ('Bolivar', 'Bolivar'), ('Finca', 'Finca'), ('Teatro', 'Teatro')], default='Colombo', max_length=9),
        ),
    ]
