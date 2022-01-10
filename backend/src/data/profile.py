from typing import List
from data.game_account import Game_account
from data.user import User
from data.picture import Picture


class Profile:
    def __init__(self, login_status: bool, age: int, country: str, name: str, bio: str, favorite_game_id: int, game_accounts: List[Game_account] = None, picture: Picture = None, user: User = None):
        self.login_status = login_status
        self.age = age
        self.country = country
        self.name = name
        self.bio = bio
        self.favorite_game_id = favorite_game_id
        if game_accounts is None:
            self.game_accounts = []
        else:
            self.game_accounts = game_accounts
        self.picture = picture
        self.user = user

    def __str__(self):
        return f"""profile
Login Status: {self.login_status}
Alter: {self.age}
Land: {self.country}
Name: {self.name}
Bio: {self.bio}
Liblings Game Id: {self.favorite_game_id}
Game Accounts: {str(self.game_accounts)}
profilebild: {str(self.picture)}
User: {str(self.user)}"""

    def get_login_status(self):
        return self.login_status

    def get_age(self):
        return self.age

    def set_age(self, age: int):
        self.age = age

    def get_country(self):
        return self.country

    def set_country(self, country: str):
        self.country = country

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_game_accounts(self):
        return self.game_accounts

    def clear_game_accounts(self):
        self.game_accounts = []

    def add_game_account(self, game_account: Game_account):
        self.game_accounts.append(game_account)

    def get_bio(self):
        return self.bio

    def set_bio(self, bio: str):
        self.bio = bio

    def get_picture(self):
        return self.picture

    def set_picture(self, picture: Picture):
        self.picture = picture

    def get_favorite_game_id(self):
        return self.favorite_game_id

    def set_favorite_game_id(self, favorite_game_id: int):
        self.favorite_game_id = favorite_game_id

    def get_user(self):
        return self.user
