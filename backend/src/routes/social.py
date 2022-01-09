from flask import Blueprint

blueprint = Blueprint("social", __name__)


@blueprint.route("/social", methods=["GET"])
def social():
    return """[
  {
    "id": 0,
    "text": "string",
    "rating": 0,
    "game_id": 0,
    "game_name": "string",
    "user_id": 0,
    "user_picture": "string"
  }
]""", 200, {"Content-Type": "application/json"}
