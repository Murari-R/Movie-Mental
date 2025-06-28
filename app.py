from flask import Flask, request, jsonify
import tmdb  # ✅ updated: direct import since it's in same folder
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/recommend", methods=["GET"])
def recommend():
    actor = request.args.get("actor")
    genre = request.args.get("genre")

    if not actor or not genre:
        return jsonify({"error": "Missing actor or genre"}), 400

    results = tmdb.search_movies(actor, genre)  # ✅ updated: use tmdb prefix
    return jsonify(results[:5])  # limit to top 5

if __name__ == "__main__":
    app.run(debug=True)
