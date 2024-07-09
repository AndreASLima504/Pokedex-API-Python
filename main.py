from fastapi import FastAPI
import uvicorn 
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
@app.get("/pokemon")
def search_pokemon(id):
    return controllers.pokemonController.request_pokemon_details(id)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
