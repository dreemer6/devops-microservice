from fastapi import FastAPI
import uvicorn
from .logic import search_wiki, phrases
from .logic import wiki as wikilogic

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API.  Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in wikipedia"""

    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve wikipedia page"""

    result = wikilogic(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """Retrieve noun phrases from wikipedia page"""

    result = phrases(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8081, host="0.0.0.0")
