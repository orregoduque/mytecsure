# Generated by Django 3.0.7 on 2021-06-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20210619_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='identidad_seguro',
            field=models.CharField(blank=True, choices=[('Colsanitas', 'Colsanitas'), ('Coomeva', 'Coomeva'), ('Seguro Social', 'Seguro Social'), ('Imbanaco', 'Imbanaco'), ('Ninguno', 'Ninguno')], default='Coomeva', max_length=13),
        ),
    ]
