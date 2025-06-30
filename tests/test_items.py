def test_create_item(client):
    response = client.post("/items/", json={"name": "TestItem", "description": "Test Desc"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "TestItem"

def test_get_items(client):
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
