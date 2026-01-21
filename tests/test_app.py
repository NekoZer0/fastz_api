from http import HTTPStatus


def test_read_zero(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo antes de vc!'}


def test_create_user(client):
    user_data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'securepassword',
    }
    response = client.post('/users/', json=user_data)
    assert response.status_code == HTTPStatus.CREATED
    response_data = response.json()
    assert response_data['username'] == user_data['username']
    assert response_data['email'] == user_data['email']
    assert 'id' in response_data
    assert 'password' not in response_data
    assert response_data['id'] == 1


def test_read_user(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    response_data = response.json()
    assert 'users' in response_data
    assert isinstance(response_data['users'], list)
    assert len(response_data['users']) >= 1


def test_update_user(client):
    updated_data = {
        'username': 'updated_username',
        'email': 'updated@example.com',
        'password': 'newsecurepassword123',
    }
    response = client.put('/users/1', json=updated_data)
    assert response.status_code == HTTPStatus.OK
    response_data = response.json()
    assert response_data['username'] == updated_data['username']
    assert response_data['email'] == updated_data['email']
    assert 'id' in response_data
    assert 'password' not in response_data
    assert response_data['id'] == 1
    assert response_data['username'] == 'updated_username'


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    response_data = response.json()
    assert response_data['id'] == 1
    assert response_data['username'] == 'updated_username'
