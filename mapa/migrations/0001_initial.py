# Generated by Django 2.2.2 on 2019-06-27 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=0, max_length=400)),
                ('altitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
    ]
