# Generated by Django 4.2.3 on 2023-07-15 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_alumno_fecha_examen'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]