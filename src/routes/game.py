from flask import Blueprint

blueprint = Blueprint("game", __name__)


@blueprint.route("/popular_games", methods=["GET"])
def popular_games():
    return """[
  {
    "id": 0,
    "name": "string",
    "releaseyear": "string",
    "description": "string",
    "website": "string",
    "creationdate": "string",
    "changedate": "string",
    "average_rating": 0,
    "picture": [
      {
        "id": 0,
        "priority": 0,
        "path": "string"
      }
    ],
    "genre": {
      "id": 0,
      "name": "string"
    },
    "publisher": {
      "id": 0,
      "name": "string",
      "website": "string",
      "picture": {
        "id": 0,
        "path": "string"
      }
    },
    "usk": {
      "id": 0,
      "name": "string",
      "classification": 0,
      "picture": {
        "id": 0,
        "path": "string"
      }
    }
  }
]""", 200, {"Content-Type": "application/json"}


@blueprint.route("/new_games", methods=["GET"])
def new_games():
    return """[
  {
    "id": 0,
    "name": "string",
    "releaseyear": "string",
    "description": "string",
    "website": "string",
    "creationdate": "string",
    "changedate": "string",
    "average_rating": 0,
    "picture": [
      {
        "id": 0,
        "priority": 0,
        "path": "string"
      }
    ],
    "genre": {
      "id": 0,
      "name": "string"
    },
    "publisher": {
      "id": 0,
      "name": "string",
      "website": "string",
      "picture": {
        "id": 0,
        "path": "string"
      }
    },
    "usk": {
      "id": 0,
      "name": "string",
      "classification": 0,
      "picture": {
        "id": 0,
        "path": "string"
      }
    }
  }
]""", 200, {"Content-Type": "application/json"}


@blueprint.route("/games", methods=["GET"])
def games():
    return """[
  {
    "id": 0,
    "name": "string",
    "releaseyear": "string",
    "description": "string",
    "website": "string",
    "creationdate": "string",
    "changedate": "string",
    "average_rating": 0,
    "picture": [
      {
        "id": 0,
        "priority": 0,
        "path": "string"
      }
    ],
    "genre": {
      "id": 0,
      "name": "string"
    },
    "publisher": {
      "id": 0,
      "name": "string",
      "website": "string",
      "picture": {
        "id": 0,
        "path": "string"
      }
    },
    "usk": {
      "id": 0,
      "name": "string",
      "classification": 0,
      "picture": {
        "id": 0,
        "path": "string"
      }
    }
  }
]""", 200, {"Content-Type": "application/json"}


@blueprint.route("/game/<id>", methods=["GET"])
def game(id):
    return """{
  "id": 0,
  "name": "string",
  "releaseyear": "string",
  "description": "string",
  "website": "string",
  "creationdate": "string",
  "changedate": "string",
  "average_rating": 0,
  "picture": [
    {
      "id": 0,
      "priority": 0,
      "path": "string"
    }
  ],
  "genre": {
    "id": 0,
    "name": "string"
  },
  "publisher": {
    "id": 0,
    "name": "string",
    "website": "string",
    "picture": {
      "id": 0,
      "path": "string"
    }
  },
  "usk": {
    "id": 0,
    "name": "string",
    "classification": 0,
    "picture": {
      "id": 0,
      "path": "string"
    }
  },
  "reviewselection": [
    {
      "id": 0,
      "text": "string",
      "rating": 0
    }
  ]
}""", 200, {"Content-Type": "application/json"}


@blueprint.route("/game/<id>/reviews", methods=["GET"])
def game_reviews(id):
    return """[
  {
    "id": 0,
    "text": "string",
    "rating": 0,
    "user_id": "string",
    "game_id": 0,
    "time_played_id": 0,
    "comments": {
      "id": 0,
      "text": "string"
    },
    "reactions": [
      {
        "id": 0,
        "count": 0
      }
    ]
  }
]""", 200, {"Content-Type": "application/json"}


@blueprint.route("/genre", methods=["GET"])
def genre():
    return """[
  {
    "id": 0,
    "name": "string",
    "description": "string"
  }
]""", 200, {"Content-Type": "application/json"}


@blueprint.route("/publisher", methods=["GET"])
def publisher():
    return """[
  {
    "id": 0,
    "name": "string",
    "description": "string",
    "website": "string",
    "picture": {
      "id": 0,
      "path": "string"
    }
  }
]""", 200, {"Content-Type": "application/json"}
