def test_create_recipe(client, auth):
    auth.login()
    response = client.post('/recipe/new', data=dict(
        title='Test Recipe', description='Test Description', ingredients='Test Ingredients', instructions='Test Instructions'
    ), follow_redirects=True)
    assert b'Test Recipe' in response.data

def test_edit_recipe(client, auth):
    auth.login()
    client.post('/recipe/new', data=dict(
        title='Test Recipe', description='Test Description', ingredients='Test Ingredients', instructions='Test Instructions'
    ), follow_redirects=True)
    response = client.post('/recipe/1', data=dict(
        title='Updated Recipe', description='Updated Description', ingredients='Updated Ingredients', instructions='Updated Instructions'
    ), follow_redirects=True)
    assert b'Updated Recipe' in response.data
