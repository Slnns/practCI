from app import app

def test_hello():
    response = app.test_client().get('/api/hello')
    assert response.status_code == 200

def test_hello_unit():
    from app import hello
    result = hello()
    assert result[0]['message'] == 'Hello World'
    assert result[1] == 200