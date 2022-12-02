from urllib import response
from fastapi.testclient import TestClient
from mylib.main import app, root, phrase, search, wiki

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API.  Call /search or /wiki"}


def test_read_search():
    response = client.get("/search/'Barack Obama'")
    assert response.status_code == 200
    assert 'Family of Barack Obama' in response.json()["result"]


def test_read_wiki():
    response = client.get("/wiki/'Barack Obama'")
    assert response.status_code == 200
    assert response.json() == {
        "result": "Barack Hussein Obama II ( (listen) bə-RAHK hoo-SAYN oh-BAH-mə; born August 4, 1961) is an American politician who served as the 44th president of the United States from 2009 to 2017."
    }


def test_read_phrases():
    response = client.get("/phrase/'Barack Obama'")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "barack hussein obama ii",
            "bə-rahk hoo-sayn oh-bah-mə",
            "august",
            "american politician",
            "44th president",
        ]
    }
