# Generated by Django 3.2.20 on 2023-07-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_information', '0004_alter_pokemon_species_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
