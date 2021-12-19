from flask import Blueprint

blueprint = Blueprint("notification", __name__)


@blueprint.route("/notifications", methods=["GET"])
def notifications():
    return """[
  {
    "id": 0,
    "text": "string",
    "read_date": "string",
    "creation_date": "string",
    "type": "string",
    "reference_id": "string"
  }
]""", 200, {"Content-Type": "application/json"}


@blueprint.route("/notification/<id>", methods=["DELETE"])
def delete_notification(id):
    return "", 200
