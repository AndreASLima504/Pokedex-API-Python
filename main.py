from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import controllers.indexController
import controllers.pokemonController
from datetime import datetime, timedelta

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens. Alterar para uma lista de domínios específicos em produção.
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)


@app.get('/index')
async def index_get_pokemon(offset: int):
    result = controllers.indexController.get_20_pokemon(offset)
    return result

# SENDS REQUEST FOR POKEMON DETAILS
# @app.route("/pokemon/<pokemon_id>", methods = ['POST'])
# def search_pokemon(pokemon_id: int):
#     return controllers.pokemonController.request_pokemon_details_pokemon_details(pokemon_id)
