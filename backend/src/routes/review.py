from datetime import datetime
from flask import Blueprint, request, jsonify
from jwt.exceptions import InvalidTokenError
from data.review import Review
from data.comment import Comment
from database import database
from util import auth

blueprint = Blueprint("review", __name__)


@blueprint.route("/review", methods=["PUT"])
def create_review():
    if not request.is_json:
        return "", 400
    req = request.get_json()
    if ("game_id" in req and "text" in req and "rating" in req and "time_played_id" in req):
        if ("Authorization" in request.headers):
            auth_header = request.headers["Authorization"]
            try:
                user_id = auth.decode(auth_header)
            except InvalidTokenError as e:
                print(e)
                return "", 401
        else:
            return "", 401
        if database.create_review(Review(1, req["text"], req["rating"],req["time_played_id"], datetime.now(), datetime.now(), False,req["game_id"],user_id)):
            return "", 200
        else:
            return "", 409
    else:
        return "", 400


@blueprint.route("/time_played", methods=["GET"])
def time_played():
    res = []
    for time_played in database.get_all_time_played():
        res.append({"id": time_played.get_id(), "unit": time_played.get_unit(
        ), "from": time_played.get_start(), "until": time_played.get_end()})
    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/comment/<id>", methods=["GET"])
def comment(id):
    comment = database.get_comment_by_id(id)
    if comment is None:
        return "",404
    res = {"id": comment.get_id(),
           "text": comment.get_text(),
           "commented_on_id": comment.get_commented_on_id(),
           "commented_on_type": comment.get_commend_on_type()
           }
    comments = comment.get_comments()
    if(len(comments) > 0):
        res_comments = []
        for com in comments:
            res_comments.append(com.get_id())
        res["commented_by_ids"] = res_comments
    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/comment/<id>", methods=["DELETE"])
def delete_comment(id):
    c_user_id = database.get_comment_by_id(id).get_user_id()
    if ("Authorization" in request.headers):
        auth_header = request.headers["Authorization"]
        try:
            user_id = auth.decode(auth_header)
            if user_id != c_user_id:
                return "", 401
        except InvalidTokenError as e:
            print(e)
            return "", 401
    else:
        return "", 401
    database.delete_comment(id)
    return "", 200


@blueprint.route("/comment", methods=["PUT"])
def create_comment():
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
    else:
        return "", 401
    if "text" in req and "commented_on_type" in req and "commented_on_id" in req:
        comment = Comment(1, req["text"], datetime.now(),
                          datetime.now(), False, req["commented_on_type"], req["commented_on_id"], user_id = user_id)
        database.create_comment(comment)
        return "", 200
    else:
        return "", 400


@blueprint.route("/review/<id>", methods=["DELETE"])
def delete_review(id):
    if ("Authorization" in request.headers):
        auth_header = request.headers["Authorization"]
        try:
            user_id = auth.decode(auth_header)
        except InvalidTokenError as e:
            print(e)
            return "", 401
    else:
        return "", 401
    if (database.delete_review(id,user_id)):
        return "",200
    else:
        return "",401

@blueprint.route("/reaction/<id>", methods=["PUT"])
def reaction(id):
    return "", 200
