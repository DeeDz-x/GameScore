from datetime import datetime


class Notification:
    def __init__(self, id: int, text: str, read_date: datetime, creation_date: datetime, type: str, reference, user_id=None):
        self.id = id
        self.text = text
        self.read_date = read_date
        self.creation_date = creation_date
        self.type = type
        self.reference = reference
        self.user_id = user_id

    def __str__(self):
        return f"""Benachrichtigungen
id: {self.id}
Text: {self.text}
Gelesen am: {self.read_date}
Erstellungsdatum: {self.creation_date}
Typ: {self.type}
Reference: {self.reference}
User id: {self.user_id}"""

    def get_id(self):
        return self.id

    def get_text(self):
        return self.text

    def get_read_date(self):
        return self.read_date

    def get_creation_date(self):
        return self.creation_date

    def get_type(self):
        return self.type

    def get_reference(self):
        return self.reference

    def get_user_id(self):
        return self.user_id


class Comment_notification(Notification):
    def __init__(self, id, text, read_date, creation_date, comment, user_id=None):
        super().__init__(id, text, read_date, creation_date, "comment", comment, user_id)

    def __str__(self):
        return f"""Kommentar Benachrichtigungen
Benachrichtigung: {super().__str__()}
        """


class Game_notification(Notification):
    def __init__(self, id, text, read_date, creation_date, game, user_id=None):
        super().__init__(id, text, read_date, creation_date, "game", game, user_id)

    def __str__(self):
        return f"""Spiel Benachrichtigungen
Benachrichtigung: {super().__str__()}
        """


class Follow_notification(Notification):
    def __init__(self, id, text, read_date, creation_date, profile, user_id=None):
        super().__init__(id, text, read_date, creation_date, "follow", profile, user_id)

    def __str__(self):
        return f"""Folgen Benachrichtigungen
Benachrichtigung: {super().__str__()}
        """
