from django.db import models

class Pokemon(models.Model):
    pokemon_id = models.IntegerField()
    name = models.CharField(max_length=20)
    ability_name = models.CharField(max_length=20)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    species_color = models.CharField(max_length=15)
