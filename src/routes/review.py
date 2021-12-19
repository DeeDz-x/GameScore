from flask import Blueprint

blueprint = Blueprint("review", __name__)


@blueprint.route("/review", methods=["PUT"])
def review():
    return "", 200


@blueprint.route("/time_played", methods=["GET"])
def time_played():
    return """[
  {
    "id": 0,
    "unit": "string",
    "from": "string",
    "until": "string"
  }
]""", 200, {"Content-Type": "application/json"}


@blueprint.route("/comment/<id>", methods=["GET"])
def comment(id):
    return """{
  "id": 0,
  "text": "string",
  "commented_on_type": "string",
  "commented_on_id": 0,
  "commented_by_ids": [
    0
  ]
}""", 200, {"Content-Type": "application/json"}


@blueprint.route("/comment/<id>", methods=["DELETE"])
def delete_comment(id):
    return "", 200


@blueprint.route("/comment", methods=["PUT"])
def create_comment(id):
    return "", 200


@blueprint.route("/reaction/<id>", methods=["PUT"])
def reaction(id):
    return "", 200
