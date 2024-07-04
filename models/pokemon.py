from flask import Flask, request, jsonify, render_template
import requests
from datetime import datetime, timedelta

def search_20(offset):
    retrieved_pokemons = []
    for i in range(offset,(offset+20)):
        _pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json()
        pokemon = {
            "name": f"{_pokemon['forms'][0]['name']}",
            "id": f"{_pokemon['id']}",
            "thumb_image": f"{_pokemon['sprites']['other']['home']['front_default']}"
        }
        retrieved_pokemons.append(pokemon)

    return retrieved_pokemons

def search_pokemon(name):
    new_pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}').json()
    new_pokemon_species = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{name}').json()
    pokemon = {
            "name": f"{new_pokemon['forms'][0]['name']}",
            "image": f"{new_pokemon['sprites']['other']['official-artwork']['front_default']}",
            "description": f"{new_pokemon_species['flavor_text_entries'][0]['flavor_text']}"
        }
    return pokemon
