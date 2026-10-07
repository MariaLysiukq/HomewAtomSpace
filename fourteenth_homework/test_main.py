from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_create_book():
    new_book = {"title": "Automate the Boring Stuff", "author": "AI"}
    response = client.post("/books", json=new_book)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == new_book["title"]
    assert data["author"] == new_book["author"]
    assert "id" in data
    
    get_response = client.get("/books")
    assert any(book["id"] == data["id"] for book in get_response.json())

def test_get_book_by_id():
    new_book = {"title": "Fluent Python", "author": "LaloC"}
    create_response = client.post("/books", json=new_book)
    book_id = create_response.json()["id"]
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["id"] == book_id

def test_get_non_existent_book():
    response = client.get("/books/999999")
    assert response.status_code == 404

def test_delete_book():
    new_book = {"title": "Test Book", "author": "Test Author"}
    create_response = client.post("/books", json=new_book)
    book_id = create_response.json()["id"]
    delete_response = client.delete(f"/books/{book_id}")
    assert delete_response.status_code == 200 
    get_response = client.get(f"/books/{book_id}")
    assert get_response.status_code == 404

def test_delete_non_existent_book():
    response = client.delete("/books/999999")
    assert response.status_code == 404
