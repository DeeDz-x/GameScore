from flask import Blueprint

blueprint = Blueprint("list", __name__)


@blueprint.route("/list/<id>", methods=["GET"])
def list(id):
    return """{
  "id": 0,
  "name": "string",
  "games": [
    {
      "id": 0,
      "name": "string"
    }
  ]
}""", 200, {"Content-Type": "application/json"}


@blueprint.route("/list/<id>", methods=["DELETE"])
def delete_list(id):
    return "", 200


@blueprint.route("/list/<id>/<gameid>", methods=["PUT"])
def add_game(id, gameid):
    return "", 200


@blueprint.route("/list/<id>/<gameid>", methods=["DELETE"])
def delete_game(id, gameid):
    return "", 200


@blueprint.route("/list", methods=["PUT"])
def create_list(id, gameid):
    return """{
  "id": 0,
  "name": "string"
}""", 200, {"Content-Type": "application/json"}
