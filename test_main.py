from main import app

client = app.test_client()

def test_home_status_code():
    response = client.get('/')
    assert response.status_code == 200

def test_home_response():
    response = client.get('/')
    assert response.data.decode() == 'deu certo'

def test_home_content_type():
    response = client.get('/')
    assert 'text/html' in response.content_type

def test_numero_status_code():
    response = client.get('/numero')
    assert response.status_code == 200

def test_numero_range():
    response = client.get('/numero')
    numero = int(response.data.decode())
    assert 1 <= numero <= 10