import os
import requests

def obtener_noticias():
    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        return None

    url = "https://newsdata.io/api/1/news"

    params = {
        "apikey": api_key,
        "q": "bolsa OR mercados OR acciones OR economía",
        "language": "es",
        "category": "business"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except Exception:
        return None

    data = response.json()

    if "results" not in data:
        return None

    noticias = []
    for item in data["results"]:
        noticias.append({
            "title": item.get("title", "Sin título"),
            "description": item.get("description", "Sin descripción")
        })

    return noticias
