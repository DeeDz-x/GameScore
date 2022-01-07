from datetime import datetime
from flask import Blueprint, request, jsonify
import base64
import binascii
import uuid
from data.picture import Picture
from data.profile import Profile
from data.game_account import Game_account
from data.user import User
from database import database
from util import auth
from jwt.exceptions import InvalidTokenError

blueprint = Blueprint("user", __name__)


@blueprint.route("/user/<int:id>", methods=["GET"])
def user_id(id):
    res = extract_profile(database.get_user_by_id(id))
    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/user", methods=["GET"])
def user():
    if ("Authorization" in request.headers):
        auth_header = request.headers["Authorization"]
        try:
            user_id = auth.decode(auth_header)
        except InvalidTokenError as e:
            print(e)
            return "", 200
        res = extract_profile(database.get_user(user_id))
        res["username"] = database.get_user(user_id).get_user().get_username()
        res["e_mail"] = database.get_user(user_id).get_user().get_username()
    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/user", methods=["PUT"])
def user_put():
    if not request.is_json:
        return "", 400
    req = request.get_json()
    if ("Authorization" in request.headers):
        auth_header = request.headers["Authorization"]
        try:
            user_id = auth.decode(auth_header)
        except InvalidTokenError as e:
            print(e)
            return "", 200
        res = extract_profile(database.get_user(user_id))
        res["username"] = database.get_user(user_id).get_user().get_username()
        res["e_mail"] = database.get_user(user_id).get_user().get_username()

    if "age" in req and isinstance(req["age"], int):
        database.get_user(user_id).set_age(req["age"])
    if "country" in req:
        database.get_user(user_id).set_country(req["country"])
    if "name" in req:
        database.get_user(user_id).set_name(req["name"])
    if "bio" in req:
        database.get_user(user_id).set_bio(req["bio"])
    if "favorite_game_id" in req and isinstance(req["favorite_game_id"], int):
        database.get_user(user_id).set_favorite_game_id(req["favorite_game_id"])
    if "e_mail" in req:
        database.get_user(user_id).get_user().set_e_mail(req["e_mail"])
    if "accounts" in req:
        database.get_user(user_id).clear_game_accounts()
        for acc in req["accounts"]:
            database.get_user(user_id).add_game_account(Game_account(
                acc["id"], acc["type"], acc["profile"], acc["change_date"]))
    if "picture" in req:
        pic_data = req["picture"]
        print(pic_data)
        if(database.get_user(user_id).get_picture() is not None):
            path = database.get_user(user_id).get_picture().get_path()
            save_to_file(pic_data, path)
            database.get_user(user_id).get_picture().set_change_date(datetime.now())
        else:
            path = "pic/" + str(uuid.uuid4()) + ".png"
            print(save_to_file(pic_data, path))
            database.get_user(user_id).set_picture(Picture(0,path,0,datetime.now(),datetime.now()))
    # database.update_user(database.get_user(user_id))
    return "", 200



@blueprint.route("/users", methods=["GET"])
def users():
    username = request.args.get("username")
    if username is None:
        return "", 422
    res = []
    for pro in database.search_users(username):
        res.append(extract_small_profile(pro))
    return jsonify(res), 200, {"Content-Type": "application/json"}

def save_to_file(pic: str, path: str):
    """Saves base64 encoded data in pic into file at path."""
    try:
        bin = base64.b64decode(pic)
        with open(path, "wb") as pic_file:
            pic_file.write(bin)
        return True
    except (IOError,binascii.Error):
        return False

def extract_profile(profile:Profile):
    """Extracts base data from profile."""
    res = extract_small_profile(profile)
    res["bio"]= profile.get_bio()
    accs = profile.get_game_accounts()
    if accs is not None:
        res["accounts"] = []
        for acc in accs:
            res["accounts"].append(
                {"id": acc.get_id(), "type": acc.get_type(), "profile": acc.get_profile()})
    return res

def extract_small_profile(profile:Profile):
    """Extracts small base data from profile."""
    res = {
        "login_status": profile.get_login_status(),
        "country": profile.get_country(),
        "name": profile.get_name(),
        "favorite_game_id": profile.get_favorite_game_id()
    }
    pic = profile.get_picture()
    if pic is not None:
        res["picture"] = {"id": pic.get_id(),
                          "path": pic.get_path()}
    return res