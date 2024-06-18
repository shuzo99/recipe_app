def test_register(client):
    response = client.post('/register', data=dict(
        username='test', email='test@example.com', password='test', confirm_password='test'
    ), follow_redirects=True)
    assert b'Account created!' in response.data

def test_login(client):
    client.post('/register', data=dict(
        username='test', email='test@example.com', password='test', confirm_password='test'
    ), follow_redirects=True)
    response = client.post('/login', data=dict(
        email='test@example.com', password='test'
    ), follow_redirects=True)
    assert b'Welcome' in response.data
