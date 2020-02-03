# Generated by Django 3.0.2 on 2020-01-06 01:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='blog.Category', verbose_name='Categorías'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 1, 36, 59, 718823, tzinfo=utc), verbose_name='Contenido'),
        ),
    ]
