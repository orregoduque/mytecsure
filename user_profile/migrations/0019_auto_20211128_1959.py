# Generated by Django 3.0.7 on 2021-11-28 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0018_userprofile_parentesco_acudiente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='grado_estudiante',
            field=models.CharField(blank=True, choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('01 ACADEMICO', '01 ACADEMICO'), ('02 ACADEMICO', '02 ACADEMICO'), ('03 ACADEMICO', '03 ACADEMICO'), ('04 ACADEMICO', '04 ACADEMICO'), ('05 ACADEMICO', '05 ACADEMICO')], default='01', max_length=12),
        ),
    ]
