from flask import Blueprint

blueprint = Blueprint("user", __name__)


@blueprint.route("/user/<id>", methods=["GET"])
def user_id(id):
    return """{
  "login_status": true,
  "country": "string",
  "name": "string",
  "bio": "string",
  "favorite_game_id": 0,
  "picture": {
    "id": 0,
    "path": "string"
  },
  "accounts": [
    {
      "id": 0,
      "type": "string",
      "profil": "string"
    }
  ]
}""", 200, {"Content-Type": "application/json"}


@blueprint.route("/user", methods=["GET"])
def user():
    return """{
  "login_status": true,
  "age": 0,
  "country": "string",
  "name": "string",
  "bio": "string",
  "favorite_game_id": 0,
  "username": "string",
  "e_mail": "string",
  "picture": {
    "id": 0,
    "path": "string"
  },
  "accounts": [
    {
      "id": 0,
      "type": "string",
      "profil": "string"
    }
  ]
}""", 200, {"Content-Type": "application/json"}


@blueprint.route("/user", methods=["PUT"])
def user_put():
    return "", 200


@blueprint.route("/users", methods=["GET"])
def users():
    return """[
  {
    "login_status": true,
    "country": "string",
    "name": "string",
    "favorite_game_id": 0,
    "picture": {
      "id": 0,
      "path": "string"
    }
  }
]""", 200, {"Content-Type": "application/json"}
