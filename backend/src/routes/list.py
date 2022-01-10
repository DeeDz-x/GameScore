from flask import Blueprint, request, jsonify
from datetime import datetime
from data.game import Game
from data.list import List
from jwt.exceptions import InvalidTokenError
from util import auth
from database import database

blueprint = Blueprint("list", __name__)


@blueprint.route("/list/<id>", methods=["GET"])
def list(id):
    
    list = database.get_list_by_id(id)
    if list is None:
        return "", 404
    if not list.get_public():
        if ("Authorization" in request.headers):
            auth_header = request.headers["Authorization"]
            try:
                user_id = auth.decode(auth_header)
            except InvalidTokenError as e:
                print(e)
                return "", 401
            if user_id != list.get_user_id:
                return "", 401
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
    list = database.get_list_by_id(id)
    if list is None:
        return "", 200
    l_user_id = list.get_user_id()
    if ("Authorization" in request.headers):
        auth_header = request.headers["Authorization"]
        try:
            user_id = auth.decode(auth_header)
            if user_id != l_user_id:
                return "", 401
        except InvalidTokenError as e:
            print(e)
            return "", 401
    else:
        return "", 401
    database.delete_list(id)
    return "", 200


@blueprint.route("/list/<id>/<gameid>", methods=["PUT"])
def add_game(id, gameid):
    list = database.get_list_by_id(id)
    if list is None:
        return "", 401
    l_user_id = list.get_user_id()
    if ("Authorization" in request.headers):
        auth_header = request.headers["Authorization"]
        try:
            user_id = auth.decode(auth_header)
            if user_id != l_user_id:
                return "", 401
        except InvalidTokenError as e:
            print(e)
            return "", 401
    else:
        return "", 401
    database.add_game_to_list(id, gameid)
    return "", 200


@blueprint.route("/list/<id>/<gameid>", methods=["DELETE"])
def delete_game(id, gameid):
    list = database.get_list_by_id(id)
    if list is None:
        return "", 401
    l_user_id = list.get_user_id()
    if ("Authorization" in request.headers):
        auth_header = request.headers["Authorization"]
        try:
            user_id = auth.decode(auth_header)
            if user_id != l_user_id:
                return "", 401
        except InvalidTokenError as e:
            print(e)
            return "", 401
    else:
        return "", 401
    database.delete_game_in_list(id,gameid)
    return "", 200


@blueprint.route("/list", methods=["PUT"])
def create_list():
    if ("Authorization" in request.headers):
        auth_header = request.headers["Authorization"]
        try:
            user_id = auth.decode(auth_header)
        except InvalidTokenError as e:
            print(e)
            return "", 401
    if not request.is_json:
        return "", 400
    req = request.get_json()
    if "name" in req and "public" in req:
        list = List(1, req["public"], req["name"], datetime.now())
        if database.create_list(list,user_id):
            return "", 200
        else:
            return "", 409
    else:
        return "", 400
