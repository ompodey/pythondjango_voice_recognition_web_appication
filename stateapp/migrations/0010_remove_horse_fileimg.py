# Generated by Django 4.0.4 on 2022-05-01 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stateapp', '0009_alter_horse_fileimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horse',
            name='fileimg',
        ),
    ]
