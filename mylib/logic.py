import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """This is a Wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """Search Wikipedia for names"""

    results = wikipedia.search(name)
    return results


def phrases(name):
    """Returns sentiment from Wikipedia"""
    try:
        page = wiki(name)
        phrase = TextBlob(page)
        return phrase.noun_phrases
    except Exception as error:
        print(f"Error in Wikipedia response: {error}")
