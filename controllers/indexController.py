from flask import Flask, request, jsonify, render_template
import models.pokemon

def viewIndex():
    return render_template('index.html')

def get20pokemon(offset):
    # pokemonList = []
    # for pokemon in models.pokemon.search20(offset):
    #     pokemonList.append(pokemon)
    return models.pokemon.search20(offset)