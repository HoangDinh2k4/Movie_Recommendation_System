from flask import Blueprint, jsonify
from app.services.movie_service import get_movie_details
from urllib.parse import unquote


movie_bp = Blueprint("movie", __name__)

@movie_bp.route("/movie/<path:movie_title>", methods=["GET"])
def get_movie_info(movie_title):
    try:
        decoded_title = unquote(movie_title)
        movie = get_movie_details(decoded_title)
        
        if movie:
            return jsonify(movie), 200  # Bỏ header hardcode
        else:
            return jsonify({"error": "Movie not found"}), 404  # Bỏ header hardcode
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Bỏ header hardcode