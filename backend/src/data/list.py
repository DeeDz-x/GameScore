from data.game import Game
from typing import List

from routes.user import user_id


class List:

    def __init__(self, id: int, public: bool, title: str, user_id: int, game: List[Game] = None):
        self.id = id
        self.public = public
        self.title = title
        self.user_id = user_id
        if game is None:
            self.game = []
        else:
            self.game = game

    def __str__(self):
        return f"""List
            Listen id: {self.id}
            Öffentlich: {self.public}
            Titel: {self.title}
            Spiele: {self.game}
            """

    def get_id(self):
        return self.id

    def get_public(self):
        return self.public

    def get_title(self):
        return self.title

    def get_game(self):
        return self.game

    def get_user_id(self):
        return self.user_id

    def clear_game(self):
        self.game = []

    def add_game(self, game: Game):
        self.game.append(game)
