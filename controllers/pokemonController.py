from flask import Flask, request, jsonify, render_template
import models.pokemon

def view_pokemon_page():
    return render_template('pokemonPage.html')

def request_pokemon_details(name_or_id):
    return models.pokemon.search_pokemon(name_or_id)