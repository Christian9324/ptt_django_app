# Generated by Django 2.2.2 on 2019-06-27 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapa', '0002_auto_20190627_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='altitud',
            new_name='latitud',
        ),
    ]
