from flask import Blueprint

blueprint = Blueprint("register", __name__)


@blueprint.route("/register", methods=["POST"])
def register():
    return """{
  "password": "string",
  "e_mail": "string",
  "username": "string"
}""", 200, {"Content-Type": "application/json"}
