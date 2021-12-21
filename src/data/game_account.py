from datetime import datetime


class Game_account:

    def __init__(self, id: int, type, profile: str, change_date: datetime):
        self.id = id
        self.type = type
        self.profile = profile
        self.change_date = change_date

    def __str__(self):
        return f"""Game Account
            Spieleacount id: {self.id}
            Platform: {self.type}
            profile: {self.profile}
            Änderungs Datum: {self.change_date}
            """

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_profile(self):
        return self.profile

    def get_change_date(self):
        return self.change_date
