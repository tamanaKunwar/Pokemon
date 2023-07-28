import requests
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Pokemon
import json
from django.shortcuts import get_object_or_404


def save_pokemon(request, pokemon_name):
    pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(pokemon_url).json()
    species = response['species']
    species_url = species['url']
    species_response = requests.get(species_url).json()
    species_color = species_response['color']['name']

    pokemon_details = {
        'Pokemon_id': response['id'],
        'name': response['name'],
        'ability_name': response['abilities'][0]['ability']['name'],
        'height': response['height'],
        'weight': response['weight'],
        'species_color': species_color}
    obj = Pokemon(pokemon_id=pokemon_details['Pokemon_id'],
                  name=pokemon_details['name'],
                  ability_name=pokemon_details['ability_name'],
                  height=pokemon_details['height'],
                  weight=pokemon_details['weight'],
                  species_color=pokemon_details['species_color'])
    obj.save()
    return JsonResponse({
        'id': obj.id,
        'pokemon_details': pokemon_details
    })

def get_pokemon_details(request, id):
    response = Pokemon.objects.get(pk=id)
    pokemon_fetched_details = {
        'Pokemon_id': response.pokemon_id,
        'name': response.name,
        'ability_name': response.ability_name,
        'height': response.height,
        'weight': response.weight,
        'species_color': response.species_color
    }
    return JsonResponse({
        'pokemon_details': pokemon_fetched_details
    })

def update_pokemon_details(request, id):
    poke = get_object_or_404(Pokemon, pk=id)
    if request.method == 'PUT':
        data = json.loads(request.body)
        requested_name = data['pokemon_details']['name']
        requested_ability_name = data['pokemon_details']['ability_name']
        requested_height = data['pokemon_details']['height']
        requested_weight = data['pokemon_details']['weight']
        requested_species_color = data['pokemon_details']['species_color']
        poke.name, poke.ability_name, poke.height, poke.weight, poke.species_color =\
            requested_name, requested_ability_name, requested_height, requested_weight, requested_species_color
        poke.save()
    return HttpResponse({"message": "Record Updated successfully"})