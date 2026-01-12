from fastapi.testclient import TestClient

from fastz_api.app import app


def test_read_zero():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == 200  # noqa: PLR2004
    assert response.json() == {'message': 'Olá mundo antes de vc!'}
