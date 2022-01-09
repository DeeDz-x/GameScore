from datetime import datetime


class Game_rating:

    def __init__(self, id: int, name: str, min: int, max: int, step: int, creation_date: datetime, change_date: datetime):
        self.id = id
        self.name = name
        self.min = min
        self.max = max
        self.step = step
        self.creation_date = creation_date
        self.change_date = change_date

    def __str__(self):
        return f"""Game Rating
            Spiele Wertung ID: {self.id}
            Name: {self.name}
            Min Bewertung: {self.min}
            Max Bewertung: {self.max}
            Erhöhung: {self.step}
            Erstellungs Datum: {self.creation_date}
            Änderungs Datum: {self.change_date}
            """

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max

    def get_step(self):
        return self.step

    def get_creation_date(self):
        return self.creation_date

    def get_change_date(self):
        return self.change_date
