# Generated by Django 4.0.4 on 2022-05-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=122, null=True)),
                ('email', models.CharField(default='', max_length=122, null=True)),
                ('suggestion', models.CharField(default='', max_length=122, null=True)),
            ],
        ),
    ]
