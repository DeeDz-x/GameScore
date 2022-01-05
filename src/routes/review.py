from datetime import datetime
from flask import Blueprint, request, jsonify
from jwt.exceptions import InvalidTokenError
from data.review import Review
from util import auth
from data.comment import Comment

blueprint = Blueprint("review", __name__)


@blueprint.route("/review", methods=["PUT"])
def create_review():
    if not request.is_json:
        return "", 400
    req = request.get_json()
    if "id" in req and "text" in req and "rating" in req and "time played" in req:
        review = Review(1, req["text"], req["rating"],
                        req["time played"], datetime.now, datetime.now, False)
        # if database.create_review(review):
        #    return "", 200
        # else:
        #    return "", 409
        return "", 200
    else:
        return "", 400


@blueprint.route("/time_played", methods=["GET"])
def time_played():
    return """[
  {
    "id": 0,
    "unit": "string",
    "from": "string",
    "until": "string"
  }
]""", 200, {"Content-Type": "application/json"}


@blueprint.route("/comment/<id>", methods=["GET"])
def comment(id):
    comment = Comment(1, "Text", datetime.now(), datetime.now(), False,
                      Comment(2, "Text2", datetime.now(),
                              datetime.now(), False),
                      [
        Comment(3, "Texte", datetime.now(), datetime.now(), False),
        Comment(4, "Text4", datetime.now(), datetime.now(), False),
    ])  # database.get_comment_by_id()
    res = {"id": comment.get_id(),
           "text": comment.get_text(),
           "commented_on_id": comment.get_commented_on().get_id()
           }
    if isinstance(comment.get_commented_on(), Comment):
        res["commented_on_type"] = "Comment"
    else:
        res["commented_on_type"] = "Review"
    comments = comment.get_comments()
    if(len(comments) > 0):
        res_comments = []
        for com in comments:
            res_comments.append(com.get_id())
        res["commented_by_ids"] = res_comments
    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/comment/<id>", methods=["DELETE"])
def delete_comment(id):
    c_user_id = 1  # database.get_comment_by_id().get_user_id()
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
    # database.delete_comment(id)
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
        comment = Comment(1, req["text"], datetime.now,
                          datetime.now, False, req["commend_on_type"], req["commend_on_id"], user_id = user_id)
        # if database.create_comment(comment):
        #    return "", 200
        # else:
        #    return "", 409
        return "", 200
    else:
        return "", 400


@blueprint.route("/reaction/<id>", methods=["PUT"])
def reaction(id):
    return "", 200
