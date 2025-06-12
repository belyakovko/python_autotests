import requests


URL='https://api.pokemonbattle.ru/v2'
TRAINER_ID='ID_тренера'
TRAINER_NAME='Имя_тренера'

def test_status():
    response=requests.get(url=f'{URL}/trainers')
    assert response.status_code==200

def test_trainer_name():
    response=requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response.json()["data"][0]["trainer_name"]==TRAINER_NAME

