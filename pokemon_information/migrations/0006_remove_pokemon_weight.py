# Generated by Django 3.2.20 on 2023-07-28 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_information', '0005_auto_20230728_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='weight',
        ),
    ]