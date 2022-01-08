from flask import Blueprint, jsonify
from datetime import datetime
from data.comment import Comment

from data.game import Game
from data.game_account import Game_account
from data.genre import Genre
from data.profile import Profile
from data.publisher import Publisher
from data.review import Review
from data.user import User
from data.usk import Usk
from database import database



blueprint = Blueprint("game", __name__)


@blueprint.route("/popular_games", methods=["GET"])
def popular_games():
    games  = database.get_popular_games()
    res = []
    for game in games:
        res.append(extract_game(game))
    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/new_games", methods=["GET"])
def new_games():
    games  = database.get_new_game()
    res = []
    for game in games:
        res.append(extract_game(game))
    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/games", methods=["GET"])
def games():
    # TODO
    game = database.get_game_by_id(id)
    res = extract_game(game)
    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/game/<id>", methods=["GET"])
def game(id):
    game = database.get_game_by_id(id)
    res = extract_game(game)
    revs = game.get_review()
    if revs is not None:
        res["review"] = []
        for rev in revs:
            res["review"].append(
                {"id": rev.get_id(), "text": rev.get_text(), "rating": rev.get_rating()}
            )
    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/game/<id>/reviews", methods=["GET"])
def game_reviews(id):
    game = Game(
        1,
        "Far cry 3",
        2022,
        "Ein Intressantes spiel",
        "Karl Müller",
        datetime.now(),
        datetime.now(),
        Publisher(1, "Test Name", "Test Beschreibung", "Test Webseite"),
        Usk(1, "18", 1),
        genre=[Genre(1, "Shooter", "Es geht um waffen gewalt", datetime.now())],
        review=[
            Review(
                1,
                "Test Text",
                3,
                1,
                datetime.now(),
                datetime.now(),
                False,
                [Comment(1, "Test Text 2", datetime.now, datetime.now, False)],
            )
        ],
    )

    profile = Profile(
        True,
        20,
        "Deutschland",
        "Karl Müller",
        "Bio",
        3,
        [Game_account(1, "Steam", "KARLMÜLLERXX", "date")],
        user=User(1, "Karl Müller", "Mail", "pass", datetime.now()),
    )  # = database.get_review_by_id(id)

    res = {
        "id": game.get_review()[0].get_id(),
        "text": game.get_review()[0].get_text(),
        "rating": game.get_review()[0].get_rating(),
        "user_id": profile.get_user().get_id(),
        "game_id": game.get_id(),
        "time_played_id": game.get_review()[0].get_time_played_id(),
    }
    comment = game.get_review()[0].get_comments()
    if comment is not None:
        res["comment"] = {
            "id": game.get_review()[0].get_comments()[0].get_id(),
            "text": game.get_review()[0].get_comments()[0].get_text(),
        }
    return jsonify(res), 200, {"Content-Type": "application/json"}

    # "reactions": [
    #  {
    #    "id": 0,
    #    "count": 0
    #  }


@blueprint.route("/genre", methods=["GET"])
def genre():
    genre = Genre(
        1, "shooter", "Es geht um waffen gewalt", datetime.now()
    )  # = database.get_genre_by_id(id)
    res = {
        "id": genre.get_id(),
        "name": genre.get_name(),
        "descrition": genre.get_description(),
    }
    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/publisher", methods=["GET"])
def publisher():
    # = database.get_publisher_by_id(id)
    publisher = Publisher(1, "Test Name", "Test Beschreibung", "Test Webseite")
    res = {
        "id": publisher.get_id(),
        "name": publisher.get_name(),
        "description": publisher.get_description(),
        "website": publisher.get_website(),
    }
    pic = publisher.get_picture()
    if pic is not None:
        res["picture"] = {"id": pic.get_id(), "path": pic.get_path()}
    return jsonify(res), 200, {"Content-Type": "application/json"}


def extract_game(game: Game):
    """Extracts base data from game."""
    res = {
        "id": game.get_id(),
        "name": game.get_name(),
        "releaseyear": game.get_release(),
        "description": game.get_description(),
        "website": game.get_website(),
        "creationdate": game.get_creation_date().strftime("%d/%m/%Y, %H:%M:%S")
        # "average_rating": database.get_game_rating(id)?
    }
    pics = game.get_picture()
    if pics is not None:
        res["picture"] = []
        for pic in pics:
            res["picture"] = {"id": pic.get_id(), "path": pic.get_path()}
    pub = game.get_publisher()
    if pub is not None:
        res["publisher"] = {
            "id": pub.get_id(),
            "name": pub.get_name(),
            "website": pub.get_website(),
        }
        pic_pub = pub.get_picture()
        if pic_pub is not None:
            res["publisher"]["picture"] = {
                "id": pic_pub.get_id(),
                "path": pic_pub.get_path(),
            }
    usk = game.get_usk()
    if usk is not None:
        res["usk"] = {
            "id": usk.get_id(),
            "name": usk.get_name(),
            "classification": usk.get_classification(),
        }
        pic_usk = usk.get_picture()
        if pic_usk is not None:
            res["usk"]["pictrue"] = {"id": pic_usk.get_id(), "path": pic_usk.get_path()}
    gen = game.get_genre()
    if gen is not None:
        res["genre"] = {"id": gen.get_id(), "name": gen.get_name()}
    return res
