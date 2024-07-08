import models.pokemon


def get_20_pokemon(offset):
    return models.pokemon.search_20(offset)