from datetime import datetime
from typing import List


class Comment:

    def __init__(self, id: int, text: str, creation_date: datetime, change_date: datetime, deleted: bool, commented_on_type: str, commented_on_id=None, comments=None, user_id=None):
        self.id = id
        self.text = text
        self.creation_date = creation_date
        self.change_date = change_date
        self.deleted = deleted
        self.commented_on_id = commented_on_id
        if comments is None:
            self.comments = []
        else:
            self.comments = comments
        self.user_id = user_id
        self.commented_on_type = commented_on_type

    def __str__(self):
        return f"""Kommentar
id: {self.id}
Text: {self.text}
Erstellungsdatum: {self.creation_date}
Änderungsdatum: {self.change_date}
Gelöscht?: {self.deleted}
Kommentare: {str(self.comments)}
User id: {self.user_id}"""

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

    def get_commented_on_id(self):
        return self.commented_on_id

    def get_comments(self):
        return self.comments

    def get_user_id(self):
        return self.user_id

    def get_commend_on_type(self):
        return self.commented_on_type
