# Generated by Django 3.0.7 on 2021-11-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20210619_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('SD', 'SD')], max_length=3),
        ),
    ]