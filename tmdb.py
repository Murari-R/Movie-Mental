import requests

TMDB_API_KEY = "d80a462c77815a7697ce7fcdf88f5620"

def search_movies(actor_name, genre_name):
    # Step 1: Get actor ID
    actor_resp = requests.get(f"https://api.themoviedb.org/3/search/person", params={
        "api_key": TMDB_API_KEY,
        "query": actor_name
    }).json()
    if not actor_resp["results"]:
        return []

    actor_id = actor_resp["results"][0]["id"]

    # Step 2: Get genre list and find genre ID
    genre_resp = requests.get(f"https://api.themoviedb.org/3/genre/movie/list", params={
        "api_key": TMDB_API_KEY,
    }).json()
    genre_id = next((g["id"] for g in genre_resp["genres"] if g["name"].lower() == genre_name.lower()), None)

    # Step 3: Discover movies by actor + genre
    discover = requests.get(f"https://api.themoviedb.org/3/discover/movie", params={
        "api_key": TMDB_API_KEY,
        "with_people": actor_id,
        "with_genres": genre_id,
        "sort_by": "popularity.desc"
    }).json()

    return discover.get("results", [])
