# Generated by Django 4.2.3 on 2023-07-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='nota',
            field=models.IntegerField(null=True),
        ),
    ]
