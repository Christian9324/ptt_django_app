# Generated by Django 2.2.2 on 2019-06-27 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='altitud',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='longitud',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
