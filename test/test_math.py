from fastapi.testclient import TestClient
from main import app

def test_get_post_number_correct():
    client = TestClient(app)

    response = client.get(
        '/api/v1/number/66'
    )
    assert response.status_code == 200
    data = response.json()
    assert data['number_plus_one'] == 67