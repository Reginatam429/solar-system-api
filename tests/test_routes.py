import pytest 

def test_add_two_planets(client):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()
    #Assert
    assert response.status_code == 200
    #assert response_body == []