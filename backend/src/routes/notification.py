from datetime import datetime
from flask import Blueprint, request, jsonify
from data.game import Game
from data.notification import Game_notification
from util import auth
from jwt.exceptions import InvalidTokenError

from routes.user import user_id

blueprint = Blueprint("notification", __name__)


@blueprint.route("/notifications", methods=["GET"])
def notifications():
    if ("Authorization" in request.headers):
        auth_header = request.headers["Authorization"]
        try:
            user_id = auth.decode(auth_header)
        except InvalidTokenError as e:
            print(e)
            return "", 401
    else:
        return "", 401
    notifications = [Game_notification(1, "neues Spiel", datetime.now(), datetime.now(), Game(1, "Spiel", datetime.now(
    ), "Bescheibung", "web", datetime.now(), datetime.now()))]  # database.get_notifications(user_id)
    res = []
    for notification in notifications:
        res.append({"id": notification.get_id(),
                    "text": notification.get_text(),
                    "read_date": notification.get_read_date(),
                    "creation_date": notification.get_creation_date(),
                    "type": notification.get_type(),
                    "reference_id": notification.get_reference().get_id()})
    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/notification/<id>", methods=["DELETE"])
def delete_notification(id):
    n_user_id = 1 #database.get_notification_by_id().get_user_id()
    if ("Authorization" in request.headers):
        auth_header = request.headers["Authorization"]
        try:
            user_id = auth.decode(auth_header)
            if user_id != n_user_id:
                return "", 401
        except InvalidTokenError as e:
            print(e)
            return "", 401
    else:
        return "", 401
    #database.delete()
    return "", 200
