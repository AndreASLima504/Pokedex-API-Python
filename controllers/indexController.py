from flask import Flask, request, jsonify, render_template
import models.pokemon

def viewIndex():
    return render_template('index.html')

def get20pokemon(offset):
    return models.pokemon.search20(offset)