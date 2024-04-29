import requests

def test_get_todo():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1') # uzklausa tinklalapiui
    assert response.status_code == 200
    data = response.json()
    print(response.json()) # suzinom raktazodzius
    print(type(response.json()))
    assert data['userId'] == 1
    assert 'title' in data
    assert 'delectus' in data['title']

test_get_todo()