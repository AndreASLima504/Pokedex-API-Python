from flask import Flask, request, jsonify, render_template
import models.pokemon

def viewPokemonDetails():
    return render_template('pokemonPage.html')

def searchPokemonDetails(name):
    return models.pokemon.searchPokemon(name)