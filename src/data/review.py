

class Review:
    def __init__(self, id, text, rating, creation_date, change_date, deleted, comments=[]):
        self.id = id
        self.text = text
        self.rating = rating
        self.creation_date = creation_date
        self.change_date = change_date
        self.deleted = deleted
        self.comments = comments

    def __str__(self):
        return f"""Review
id: {self.id}
Text: {self.text}
Rating: {self.rating}
Erstellungsdatum: {self.creation_date}
Änderungsdatum: {self.change_date}
Gelöscht?: {self.deleted}
Kommentar: {self.comments}"""

    def get_id(self):
        return self.id

    def get_text(self):
        return self.text

    def get_rating(self):
        return self.rating

    def get_creation_date(self):
        return self.creation_date

    def get_change_date(self):
        return self.change_date

    def get_deleted(self):
        return self.deleted

    def get_comments(self):
        return self.comments
