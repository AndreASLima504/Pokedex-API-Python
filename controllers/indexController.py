import models.pokemon
import concurrent.futures

def get_20_pokemon(offset):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(models.pokemon.search_pokemon, i) for i in range(offset, offset + 20)]
        pokemons = [f.result() for f in concurrent.futures.as_completed(futures) if f.result() is not None]


    results = sorted(pokemons, key=lambda x: int(x['id']))

    return results