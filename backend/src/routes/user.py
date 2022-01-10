from datetime import datetime
from flask import Blueprint, request, jsonify
import base64
import binascii
import uuid
from data.picture import Picture
from data.profile import Profile
from data.game_account import Game_account
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
            return "", 401
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
            return "", 401
    user = database.get_user(user_id)
    change = False
    if "age" in req and isinstance(req["age"], int):
        user.set_age(req["age"])
        change = True
    if "country" in req:
        user.set_country(req["country"])
        change = True
    if "name" in req:
        user.set_name(req["name"])
        change = True
    if "bio" in req:
        user.set_bio(req["bio"])
        change = True
    if "e_mail" in req:
        user.get_user().set_e_mail(req["e_mail"])
        change = True
    if "accounts" in req:
        user.clear_game_accounts()
        for acc in req["accounts"]:
            user.add_game_account(Game_account(0, acc["type"], acc["profile"],datetime.now()))
        change = True
    if "picture" in req:
        pic_data = req["picture"]
        print(pic_data)
        if(user.get_picture() is not None):
            path = user.get_picture().get_path()
            save_to_file(pic_data, path)
            user.get_picture().set_change_date(datetime.now())
        else:
            path = str(uuid.uuid4()) + ".png"
            print(save_to_file(pic_data, "pic/" + path))
            user.set_picture(Picture(0,path,0,datetime.now(),datetime.now()))
        change = True
    if change:
        database.update_user(user)
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