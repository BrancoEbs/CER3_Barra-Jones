# Generated by Django 4.2 on 2024-07-08 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_registroproduccion_hora_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='registroproduccion',
            name='total_litros',
            field=models.FloatField(default=0),
        ),
    ]