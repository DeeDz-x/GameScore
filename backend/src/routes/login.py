from flask import Blueprint, request, jsonify
from util import auth
from jwt.exceptions import InvalidTokenError
from database import database

blueprint = Blueprint("login", __name__)


@blueprint.route("/login", methods=["POST"])
def login():
    if (not request.is_json):
        return "", 400
    req = request.get_json()
    if ("e_mail" in req and "password" in req):
        user_id = database.login(req["e_mail"],req["password"])
        if (user_id is not None):
            return auth.encode(user_id),200
    return "", 404


@blueprint.route("/logout", methods=["POST"])
def logout():
    if ("Authorization" in request.headers):
        auth_header = request.headers["Authorization"]
        try:
            user_id = auth.decode(auth_header)
        except InvalidTokenError as e:
            print(e)
            return "", 200
        print(user_id)
        database.logout(user_id)
    return "", 200


@blueprint.route("/forgot", methods=["POST"])
def forgot():
    return """{
  "e-mail": "string"
}""", 200, {"Content-Type": "application/json"}


@blueprint.route("/update_password", methods=["POST"])
def update_password():
    return "", 200
