import requests
import json
token = 'edb9e77972a02c2fd5dc71d679e20e8e'
'''respons = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": 'Коржик',
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})'''
'''print(respons.text)'''
'''respons_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 2340,
    "name": "РжанойКоржик",
    "photo": ""
})'''
'''print(respons_put.text)'''
respons_post = requests.post('https://pokemonbattle.me:5000//trainers/addPokebol', headers={'trainer_token' : token}, json={
    "pokemon_id": "2340"
})
print(respons_post.text)
