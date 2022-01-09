from flask import Blueprint, request, jsonify
from data.game import Game
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
    title = request.args.get("title")
    if title is None:
        return "",422
    genre = request.args.get("genre")
    release_year = request.args.get("releaseyear")
    publisher = request.args.get("publisher")
    games = database.search_games(title,genre,release_year,publisher)
    res = []
    for game in games:
        res.append(extract_game(game))
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
    reviews = database.get_reviews_by_game_id(id)
    res = []
    for review in reviews:
        rev =  {
            "id": review.get_id(),
            "text": review.get_text(),
            "rating": review.get_rating(),
            "user_id": review.get_user_id(),
            "game_id": id,
            "time_played_id": review.get_time_played_id(),
            "comments": [],
        }
        for com in review.get_comments():
            rev["comments"].append({
                "id":com.get_id(),
                "text": com.get_text(),
                "user_id":com.get_user_id(),
            })
        res.append(rev)
    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/genre", methods=["GET"])
def genre():
    res = []
    for genre in database.get_all_genres():
        res.append({
            "id": genre.get_id(),
            "name": genre.get_name(),
            "descrition": genre.get_description(),
        })
    return jsonify(res), 200, {"Content-Type": "application/json"}


@blueprint.route("/publisher", methods=["GET"])
def publisher():
    res = []
    for publisher in database.get_all_publisher():
        pub = {
            "id": publisher.get_id(),
            "name": publisher.get_name(),
            "description": publisher.get_description(),
            "website": publisher.get_website(),
        }
        pic = publisher.get_picture()
        if pic is not None:
            pub["picture"] = {"id": pic.get_id(), "path": pic.get_path()}
        res.append(pub)
    return jsonify(res), 200, {"Content-Type": "application/json"}


def extract_game(game: Game):
    """Extracts base data from game."""
    res = {
        "id": game.get_id(),
        "name": game.get_name(),
        "releaseyear": game.get_release(),
        "description": game.get_description(),
        "website": game.get_website(),
        "creationdate": game.get_creation_date().strftime("%d/%m/%Y, %H:%M:%S"),
        "average_rating": database.get_average_rating(game.get_id())
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
