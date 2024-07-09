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
    print(type(new_pokemon_species['flavor_text_entries'][0]))
    
    for dict in new_pokemon_species['flavor_text_entries']:
        english_txt = ''
        if dict['language']['name'] == 'en':
            english_txt = dict["flavor_text"]
            break
    print(english_txt)

    species_desc = ''
    for dict in new_pokemon_species['genera']:
        if dict['language']['name'] == 'en':
            species_desc = dict['genus']
            break 

    types = []
    for dict in new_pokemon['types']:
        types.append(dict['type']['name'])
    
    pokemon = {
            "id": new_pokemon['id'],
            "name": f"{new_pokemon['forms'][0]['name']}",
            "image": f"{new_pokemon['sprites']['other']['official-artwork']['front_default']}",
            "species_desc": species_desc,
            "types": types,
            "flavor-text": english_txt,
            "color": f"{new_pokemon_species['color']['name']}"
        }
    return pokemon

