# Generated by Django 3.2.20 on 2023-07-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_information', '0006_remove_pokemon_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
