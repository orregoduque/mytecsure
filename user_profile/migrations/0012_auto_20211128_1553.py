# Generated by Django 3.0.7 on 2021-11-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0011_userprofile_tipodoc_estudiante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='identidad_seguro',
            field=models.CharField(blank=True, choices=[('ASMESALUD', 'ASMESALUD'), ('CAFESALUD', 'CAFESALUD'), ('CAPRECOM', 'CAPRECOM'), ('CEDIMA', 'CEDIMA'), ('COLSANITAS', 'COLSANITAS'), ('COMFAMILIAR', 'COMFAMILIAR'), ('COMFENALCO', 'COMFENALCO'), ('COOSALUD', 'COOSALUD'), ('COOMEVA', 'COOMEVA'), ('COSMITET', 'COSMITET'), ('CRUZ BLANCA', 'CRUZ BLANCA'), ('EMAVI', 'EMAVI'), ('EMSANAR', 'EMSANAR'), ('LA POLICIA', 'LA POLICIA'), ('MEDIMAS', 'MEDIMAS'), ('NUEVA EPS', 'NUEVA EPS'), ('P.N.C', 'P.N.C'), ('PONAL', 'PONAL'), ('PREVISORA', 'PREVISORA'), ('S.O.S', 'S.O.S'), ('SALUD TOTAL', 'SALUD TOTAL'), ('SALUDCOOP', 'SALUDCOOP'), ('SANIDAD MILITAR', 'SANIDAD MILITAR'), ('SANITAS', 'SANITAS'), ('SIN DEFINIR', 'SIN DEFINIR'), ('SISBEN', 'SISBEN'), ('SURAMERICANA', 'SURAMERICANA')], default='Coomeva', max_length=15),
        ),
    ]
