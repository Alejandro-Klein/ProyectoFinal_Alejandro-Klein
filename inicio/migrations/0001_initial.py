# Generated by Django 4.2.3 on 2023-07-12 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('materia', models.CharField(max_length=20)),
                ('nota', models.IntegerField()),
            ],
        ),
    ]
