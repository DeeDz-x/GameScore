from datetime import datetime
from flask import Blueprint, request, jsonify
from data.user import User
from data.usk import Usk

from routes.user import User

blueprint = Blueprint("register", __name__)


@blueprint.route("/register", methods=["POST"])

def register():
  user = User("Test", "Test@test.de", "IchHasseBrunsman",datetime.now)
  if not request.is_json:
        return "", 400
  req = request.get_json()
  if "username" in req:
    user.set_username(req["username"])
    
  return """{
  "password": "string",
  "e_mail": "string",
  "username": "string"
}""", 200, {"Content-Type": "application/json"}
