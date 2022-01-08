from data.game import Game
from typing import List


class List:

    def __init__(self, id: int, public: bool, title: str, game: List[Game] = None):
        self.id = id
        self.public = public
        self.title = title
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

    def clear_game(self):
        self.game_accounts = []

    def add_game(self, game: Game):
        self.game.append(game)