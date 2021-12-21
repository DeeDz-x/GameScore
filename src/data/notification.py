from datetime import datetime


class Notification:
    def __init__(self, id: int, text: str, read_date: datetime, change_date: datetime):
        self.id = id
        self.text = text
        self.read_date = read_date
        self.change_date = change_date

    def __str__(self):
        return f"""Benachrichtigungen
id: {self.id}
Text: {self.text}
Gelesen am: {self.read_date}
Änderungsdatum: {self.change_date}"""

    def get_id(self):
        return self.id

    def get_text(self):
        return self.text

    def get_read_date(self):
        return self.read_date

    def get_change_date(self):
        return self.change_date


class Comment_notification(Notification):
    def __init__(self, id, text, read_date, change_date, comment):
        super().__init__(id, text, read_date, change_date)
        self.comment = comment

    def __str__(self):
        return f"""Kommentar Benachrichtigungen
Benachrichtigung: {super().__str__()}
Kommentar: {str(self.comment)}
        """

    def get_comment(self):
        return self.comment


class Game_notification(Notification):
    def __init__(self, id, text, read_date, change_date, game):
        super().__init__(id, text, read_date, change_date)
        self.game = game

    def __str__(self):
        return f"""Kommentar Benachrichtigungen
Benachrichtigung: {super().__str__()}
Kommentar: {str(self.game)}
        """

    def get_comment(self):
        return self.game


class Follow_notification(Notification):
    def __init__(self, id, text, read_date, change_date, profile):
        super().__init__(id, text, read_date, change_date)
        self.profile = profile

    def __str__(self):
        return f"""Kommentar Benachrichtigungen
Benachrichtigung: {super().__str__()}
Kommentar: {str(self.profile)}
        """

    def get_comment(self):
        return self.profile
