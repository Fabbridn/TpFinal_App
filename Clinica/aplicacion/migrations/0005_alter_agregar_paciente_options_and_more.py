# Generated by Django 5.2.1 on 2025-06-11 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_avatar_buscar_paciente_paciente_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agregar_paciente',
            options={'verbose_name': 'Agregar Paciente', 'verbose_name_plural': 'Agregar Pacientes'},
        ),
        migrations.AlterField(
            model_name='agregar_paciente',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
