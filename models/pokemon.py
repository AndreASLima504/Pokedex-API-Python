from flask import Flask, request, jsonify, render_template
import requests

def search20(offset):
    retrievedPokemons = []
    for i in range(offset,offset+20):
        _pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json()
        pokemon = {
            "name": f"{_pokemon['forms'][0]['name']}",
            "id": f"{_pokemon['id']}",
            "thumbImage": f"{_pokemon['sprites']['other']['home']['front_default']}"
        }
        retrievedPokemons.append(pokemon)

    return retrievedPokemons

def searchPokemon(name):
    newPokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}').json()
    newPokemonSpecies = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{name}').json()
    pokemon = {
            "name": f"{newPokemon['forms'][0]['name']}",
            "image": f"{newPokemon['sprites']['other']['official-artwork']['front_default']}",
            "description": f"{newPokemonSpecies['flavor_text_entries'][0]['flavor_text']}"
        }
    return pokemon
