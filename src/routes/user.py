from datetime import datetime
from flask import Blueprint, request, jsonify
import base64
import binascii
import uuid
from data.picture import Picture
from data.profile import Profile
from data.game_account import Game_account
from data.user import User
#from database.database import database

blueprint = Blueprint("user", __name__)


@blueprint.route("/user/<int:id>", methods=["GET"])
def user_id(id):
    profile = Profile(True, 20, "Deutschland", "Karl Müller", "Bio", 3, [Game_account(
        1, "Steam", "KARLMÜLLERXX", "date")],user=User("Karl Müller","Mail","pass",datetime.now()))  # = database.get_user_by_id(id)
    res = extract_profile(profile)
    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/user", methods=["GET"])
def user():
    profile = Profile(True, 20, "Deutschland", "Karl Müller", "Bio", 3, [Game_account(
        1, "Steam", "KARLMÜLLERXX", "date")],user=User("Karl Müller","Mail","pass",datetime.now()))  # = database.get_user_by_id(id)
    res = extract_profile(profile)
    res["username"] = profile.get_user().get_username()
    res["e_mail"] = profile.get_user().get_username()
    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/user", methods=["PUT"])
def user_put():
    if not request.is_json:
        return "", 400
    req = request.get_json()
    profile = Profile(True, 20, "Deutschland", "Karl Müller", "Bio", 3, [Game_account(
        1, "Steam", "KARLMÜLLERXX", "date")],user=User("Karl Müller","Mail","pass",datetime.now()))  # database.get_user_by_id(id)
    if "age" in req and isinstance(req["age"], int):
        profile.set_age(req["age"])
    if "country" in req:
        profile.set_country(req["country"])
    if "name" in req:
        profile.set_name(req["name"])
    if "bio" in req:
        profile.set_bio(req["bio"])
    if "favorite_game_id" in req and isinstance(req["favorite_game_id"], int):
        profile.set_favorite_game_id(req["favorite_game_id"])
    if "e_mail" in req:
        profile.get_user().set_e_mail(req["e_mail"])
    if "accounts" in req:
        profile.clear_game_accounts()
        for acc in req["accounts"]:
            profile.add_game_account(Game_account(
                acc["id"], acc["type"], acc["profile"], acc["change_date"]))
    if "picture" in req:
        pic_data = req["picture"]
        print(pic_data)
        if(profile.get_picture() is not None):
            path = profile.get_picture().get_path()
            save_to_file(pic_data, path)
            profile.get_picture().set_change_date(datetime.now())
        else:
            path = "pic/" + str(uuid.uuid4()) + ".png"
            print(save_to_file(pic_data, path))
            profile.set_picture(Picture(0,path,0,datetime.now(),datetime.now()))
    # database.update_user(profile)
    return "", 200



@blueprint.route("/users", methods=["GET"])
def users():
    username = request.args.get("username")
    print(username)
    profile_list = [Profile(True, 20, "Deutschland", "Karl Müller", "Bio", 3, [Game_account(
        1, "Steam", "KARLMÜLLERXX", "date")],user=User("Karl Müller","Mail","pass",datetime.now())),Profile(True, 20, "Deutschland", "Karl Meier", "Bio", 3, [Game_account(
        1, "Steam", "KARLMÜLLERXX", "date")],user=User("Karl Müller","Mail","pass",datetime.now()))] #database.sreach_users(username)
    res = []
    for pro in profile_list:
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
        "favorite_game_id": profile.get_login_status()
    }
    pic = profile.get_picture()
    if pic is not None:
        res["picture"] = {"id": pic.get_id(),
                          "path": pic.get_path()}
    return res