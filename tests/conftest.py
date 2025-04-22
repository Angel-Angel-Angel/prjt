def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_users_page(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert b"John Mike" in response.data
    assert b"Angel Bello" in response.data
