import requests

URL='https://api.pokemonbattle.ru/v2'
TRAINER_ID='ID тренера'

def test_status():
    response=requests.get(url=f'{URL}/trainers')
    assert response.status_code==200

def test_trainers_id():
    response=requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response.json()["data"][0]["id"]==TRAINER_ID