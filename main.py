from flask import Flask, request, jsonify, render_template
import controllers.indexController
import controllers.pokemonController
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/home", methods = ['GET'])
def index():
    # return controllers.indexController.viewIndex()
    return render_template('index.html')

@app.route("/api/index", methods = ['POST'])
def get_pokemon_index():
    offset = request.get_json()
    result = controllers.indexController.get_20_pokemon(offset[0])
    return result


# SHOW POKEMON DETAILS PAGE
@app.route("/pokemon/<pokemon_id>", methods = ['GET'])
def show_pokemon():
    return controllers.pokemonController.view_pokemon_page()

# SENDS REQUEST FOR POKEMON DETAILS
@app.route("/pokemon", methods = ['POST'])
def search_pokemon():
    _request = request.get_json()
    return controllers.pokemonController.request_pokemon_details_pokemon_details(_request[0])

if __name__ == '__main__':
        app.run(debug=True)
