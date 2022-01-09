from datetime import datetime
from flask import Blueprint, request, jsonify
from data.user import User
from database import database


blueprint = Blueprint("register", __name__)


@blueprint.route("/register", methods=["POST"])
def register():

    if not request.is_json:
        return "", 400
    req = request.get_json()
    if "username" in req and "password" in req and "e_mail" in req:
        user = User(1, req["username"], req["e_mail"],
                    req["password"], datetime.now())
        if database.create_user(user):
            return "", 200
        else:
            return "", 409
    else:
        return "", 400
