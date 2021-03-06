# Generated by Django 3.0.7 on 2021-06-19 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointment', '0003_auto_20210618_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('actividad', models.CharField(default='interclases ', max_length=300)),
                ('lugar', models.CharField(blank=True, choices=[('Colombo', 'Colombo'), ('Americano', 'Americano'), ('Frances', 'Frances'), ('Bolivar', 'Bolivar'), ('Finca', 'Finca'), ('Teatro', 'Teatro')], max_length=9)),
                ('director', models.ForeignKey(default='director', on_delete=django.db.models.deletion.CASCADE, related_name='director_idd', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(default='student', on_delete=django.db.models.deletion.CASCADE, related_name='student_idd', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
