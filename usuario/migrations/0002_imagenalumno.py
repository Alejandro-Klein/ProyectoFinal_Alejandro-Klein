# Generated by Django 4.2.3 on 2023-07-17 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenAlumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_alumno', models.ImageField(blank=True, null=True, upload_to='img_alumnos')),
            ],
        ),
    ]
