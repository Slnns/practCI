from app import app

def test_hello():
    # Используем test_client правильно
    with app.test_client() as client:
        response = client.get('/api/hello')
        assert response.status_code == 200
        assert response.json['message'] == 'Hello World'

def test_hello_unit():
    # Импортируем внутри контекста приложения
    with app.app_context():
        from app import hello
        result = hello()
        assert result[0]['message'] == 'Hello World'
        assert result[1] == 200