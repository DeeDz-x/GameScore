from datetime import datetime


class Genre:

    def __init__(self, id: int, name: str, description: str, creation_date: datetime):
        self.id = id
        self.name = name
        self.description = description
        self.creation_date = creation_date

    def __str__(self):
        return f"""Genre
            ID: {self.id}
            Genre: {self.name}
            Beschreibung: {self.description}
            Erstellungs Datum: {self.creation_date}
            """

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_creation_date(self):
        return self.creation_date
