# Generated by Django 4.0.4 on 2022-05-01 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stateapp', '0004_alter_horse_email_alter_horse_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='fileimg',
            field=models.ImageField(default='', null=True, upload_to='home/images'),
        ),
    ]
