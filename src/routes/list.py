from flask import Blueprint, request, jsonify
from datetime import datetime
from data.game import Game
from data.list import List

blueprint = Blueprint("list", __name__)


@blueprint.route("/list/<id>", methods=["GET"])
def list(id):
    list = List(1, False, "Test Titel", [Game(1, "Test Game", datetime.now(),
                "Ein Test spiel", "Test Website", datetime.now(), datetime.now())])  # database.get_list_by_id()
    res = {"id": list.get_id(),
           "title": list.get_title()
           }
    gams = list.get_game()
    if gams is not None:
        res["game"] = []
        for gam in gams:
            res["game"].append({"id": gam.get_id(),
                                "name": gam.get_name()})

    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/list/<id>", methods=["DELETE"])
def delete_list(id):
    return "", 200


@blueprint.route("/list/<id>/<gameid>", methods=["PUT"])
def add_game(id, gameid):
    if not request.is_json:
        return "", 400
    list = List(1, False, "Test Titel", [Game(1, "Test Game", datetime.now(),
                "Ein Test spiel", "Test Website", datetime.now(), datetime.now())])  # database.get_list_by_id()
    req = request.get_json()
    if "game" in req:
        # list.clear_game()
        for gem in req["game"]:
            list.add_game(Game(gem["id"], gem["name"], gem["release"], gem["description"],
                          gem["website"], gem["creation_date"], gem["change_date"]))
    # database.add_game_to_list_by_id(id, gameid)
    return "", 200


@blueprint.route("/list/<id>/<gameid>", methods=["DELETE"])
def delete_game(id, gameid):
    return "", 200


@blueprint.route("/list", methods=["PUT"])
def create_list():
    if not request.is_json:
        return "", 400
    req = request.get_json()
    if "id" in req and "name" in req and "öffentlich" in req:
        list = List(1, req["name"], req["öffentlich"], datetime.now())
        # if database.create_list(list):
        #    return "", 200
        # else:
        #    return "", 409
        return "", 200
    else:
        return "", 400
