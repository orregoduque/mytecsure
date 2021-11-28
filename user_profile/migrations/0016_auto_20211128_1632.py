# Generated by Django 3.0.7 on 2021-11-28 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0015_auto_20211128_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='barrio_acudiente',
            new_name='direccion_mama',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='comuna_acudiente',
            new_name='direccion_papa',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='comuna_estudiante',
            new_name='nombre_mama',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='email_estudiante',
            new_name='nombre_papa',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ocupacion_papa',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]