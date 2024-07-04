from flask import Flask, request, jsonify, render_template
import models.pokemon

def view_index():
    return render_template('index.html')

def get_20_pokemon(offset):
    return models.pokemon.search_20(offset)