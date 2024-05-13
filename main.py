from flask import Flask, request, jsonify, render_template
import controllers.indexController
import controllers.pokemonController

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def index():
    return controllers.indexController.viewIndex()

@app.route("/", methods = ['POST'])
def getPokemonIndex():
    offset = request.get_json()
    return controllers.indexController.get20pokemon(offset[0])

# SHOW POKEMON DETAILS PAGE
@app.route("/pokemon", methods = ['GET'])
def showPokemon():
    return controllers.pokemonController.viewPokemonDetails()

# SENDS REQUEST FOR POKEMON DETAILS
@app.route("/pokemon", methods = ['POST'])
def searchPokemon():
    _request = request.get_json()
    return controllers.pokemonController.searchPokemonDetails(_request[0])

if __name__ == '__main__':
        app.run(debug=True)
