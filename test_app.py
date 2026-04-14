from app import app

def test_hello():
    with app.test_client() as client:
        response = client.get('/api/hello')
        assert response.status_code == 200
        assert response.json['message'] == 'Hello World'

def test_hello_unit():
    with app.app_context():
        from app import hello
        response = hello()
        # Response object имеет атрибуты, а не индексы
        assert response.status_code == 200
        assert response.json['message'] == 'Hello World'