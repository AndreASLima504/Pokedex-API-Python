import requests
from datetime import datetime, timedelta


def search_pokemon(name):
    new_pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}').json()
    pokemon = {
            "name": f"{new_pokemon['forms'][0]['name']}",
            "id": new_pokemon['id'],
            "thumb_image": f"{new_pokemon['sprites']['other']['home']['front_default']}"
        }
    return pokemon

def search_pokemon_details(name):
    new_pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}').json()
    new_pokemon_species = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{name}').json()
    pokemon = {
            "name": f"{new_pokemon['forms'][0]['name']}",
            "image": f"{new_pokemon['sprites']['other']['official-artwork']['front_default']}",
            "description": f"{new_pokemon_species['flavor_text_entries'][0]['flavor_text']}"
        }
    return pokemon

