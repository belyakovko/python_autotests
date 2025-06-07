import requests

URL='https://api.pokemonbattle.ru/v2'
HEADER={'content-type': 'application/json',  'trainer_token': 'Токен_Тренера'}
TRAINER_ID='ID тренера'

body_create_pokemon={
    "name": "generate", 
    "photo_id": -1   
}
body_rename_pokemon={
    "pokemon_id": "ID покемона",
    "name": "Новое имя покемона",
    "photo_id": 1
}
body_rename_pokemon_patch={
    "pokemon_id": "ID покемона",
    "name": "Новое имя покемона"
}
body_pokemon_in_pokeball={
    "pokemon_id": "ID покемона"
    }
pokemon_id=0
create_pokemon=requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create_pokemon)
print(create_pokemon.text)
rename_pokemon=requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_rename_pokemon)
print(rename_pokemon.text)
rename_pokemon=requests.patch(url=f'{URL}/pokemons', headers=HEADER, json=body_rename_pokemon_patch)
print(rename_pokemon.text)
pokemon_in_pokeball=requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokemon_in_pokeball)
print(pokemon_in_pokeball.text)