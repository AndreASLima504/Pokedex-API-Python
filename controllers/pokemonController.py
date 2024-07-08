import models.pokemon


def request_pokemon_details(name_or_id):
    return models.pokemon.search_pokemon(name_or_id)