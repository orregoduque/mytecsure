# Generated by Django 3.0.7 on 2022-10-24 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0008_auto_20221022_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='director',
        ),
    ]
