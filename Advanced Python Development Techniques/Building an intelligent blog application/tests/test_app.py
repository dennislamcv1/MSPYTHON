# CODE SHOULD NOT BE MODIFIED

import json

def test_posts_initialized_as_empty_list():
    """
    Verify that the posts variable is initialized as an empty list.
    This test ensures that posts starts as an empty list ([]), 
    which is the correct initial state for the application.
    """
    from app import posts
    assert posts == []

def test_get_posts(client):
    """
    Test getting all posts.

    Verifies that the '/posts' endpoint:
    - Returns a 200 OK status code.
    - Returns an empty list when there are no posts.
    """
    response = client.get('/posts')
    assert response.status_code == 200
    assert response.json == []

def test_create_post(client):
    """
    Test creating a new post.

    Verifies that the '/posts' endpoint:
    - Accepts a POST request with valid data (title and content).
    - Returns a 201 Created status code.
    - Returns the newly created post as JSON.
    """
    data = {'title': 'Test Post', 'content': 'Test Content'}
    response = client.post('/posts', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert response.json['title'] == 'Test Post'
    assert response.json['content'] == 'Test Content'

def test_create_post_invalid_data(client):
    """
    Test creating a post with invalid data.

    Verifies that the '/posts' endpoint:
    - Returns a 400 Bad Request status code when data is missing 
      or invalid (e.g., missing title or content).
    - Returns an error message in the JSON response.
    """
    response = client.post('/posts', data=json.dumps({}), content_type='application/json')
    assert response.status_code == 400
    assert 'error' in response.json

def test_create_post_mock_posts(client, mocker):
    """
    Test creating a new post with a mocked POSTS list.

    This test mocks the 'app.posts' list to isolate the 'create_post'
    function and ensure it correctly adds a new post to the list.

    Verifies that:
    - The '/posts' endpoint returns a 201 Created status code.
    - The returned JSON includes the correct post data and an ID.
    - The new post is added to the mocked 'POSTS' list.
    """
    mock_posts = []
    mocker.patch('app.posts', mock_posts)

    data = {'title': 'Test Post 1', 'content': 'Test Content 1'}
    response = client.post('/posts', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert response.json['id'] == 1
    assert response.json['title'] == 'Test Post 1'
    assert response.json['content'] == 'Test Content 1'

    data = {'title': 'Test Post 2', 'content': 'Test Content 2'}
    response = client.post('/posts', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert response.json['id'] == 2
    assert response.json['title'] == 'Test Post 2'
    assert response.json['content'] == 'Test Content 2'

    assert mock_posts == [
        {'id': 1, 'title': 'Test Post 1', 'content': 'Test Content 1'},
        {'id': 2, 'title': 'Test Post 2', 'content': 'Test Content 2'}
    ]