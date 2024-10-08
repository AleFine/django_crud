# Generated by Django 5.0.7 on 2024-08-11 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasApp', '0002_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['apellidos', 'nombre']},
        ),
    ]
