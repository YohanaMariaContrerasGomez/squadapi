from pydoc import cli
from fastapi.testclient import TestClient
from main import app

def test_create_joke_ok():
    client = TestClient(app)

    joke = {
        'texto': 'With one steely eyed glare, Chuck Norris turned Atilla the Hun into whats now known as the Easter Bunny.'
    }

    response = client.post(
        '/api/v1/joke/',
        json=joke,
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data['texto'] == joke['texto']

def test_get_joke_ok():
    client = TestClient(app)

    response = client.get(
        '/api/v1/joke/'
    )
    assert response.status_code == 200
    data = response.json()
