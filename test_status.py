import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

def test_piese_of_body():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id' : '1425'})
    assert response.json()['trainer_name'] == 'MIKHAIL'

@pytest.mark.parametrize('kye, value', [('trainer_name', 'MIKHAIL'),('city', 'Moscow')])

def test_parametrs_body(kye, value):
    host = 5000
    respons = requests.get(f'https://pokemonbattle.me:{host}/trainers', params = {'trainer_id' : '1425'})
    assert respons.json()[kye] == value

    name_of_trainer = respons.json()['trainer_name']