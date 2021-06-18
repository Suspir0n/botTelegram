def test_post_user(app, client):
    mock_request_data = {
        "uid": 1,
        "data": {
            "name": "Teste",
            "phone": "71983620502",
            "text": "Hello my friend"
        },
        "date": 1621085772
    }
    response = client.post('/users', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully registered'
    assert expected in response.get_data(as_text=True)


def test_get_users(app, client):
    response = client.get('/users')
    assert response.status_code == 200
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_get_user_by_id(app, client):
    response = client.get('/users/1')
    assert response.status_code == 201
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_update_user(app, client):
    mock_request_data = {
        "uid": 1,
        "data": {
            "name": "Testando",
            "phone": "71983620502",
            "text": "Hello my friend"
        },
        "date": 1621085772
    }
    response = client.put('/users/1', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully updated'
    assert expected in response.get_data(as_text=True)


def test_delete_user(app, client):
    response = client.delete('/users/1')
    assert response.status_code == 404
    expected = 'unable to delete'
    assert expected in response.get_data(as_text=True)