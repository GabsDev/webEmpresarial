# Generated by Django 3.0.2 on 2020-01-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Subtítulo')),
                ('content', models.CharField(max_length=200, verbose_name='Contenido')),
                ('image', models.CharField(max_length=200, verbose_name='Imagen')),
                ('created', models.CharField(max_length=200, verbose_name='Fecha de creación')),
                ('updated', models.CharField(max_length=200, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['-created'],
            },
        ),
    ]
