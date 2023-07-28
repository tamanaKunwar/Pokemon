# Generated by Django 3.2.20 on 2023-07-28 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_information', '0002_pokemon_ability_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='species_color',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
