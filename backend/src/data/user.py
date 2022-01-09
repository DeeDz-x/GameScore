from datetime import datetime


class User:
    def __init__(self, id:int, username:str, e_mail:str, password:str, register_date:datetime):
        self.username = username
        self.e_mail = e_mail
        self.password = password
        self.register_date = register_date
        self.id = id

    def __str__(self):
        return f"""User
Username: {self.username}
E-Mail: {self.e_mail}
Passwort: {self.password}
Registrierungsdatum: {self.register_date}"""

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_e_mail(self):
        return self.e_mail

    def set_e_mail(self, e_mail):
        self.e_mail = e_mail

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_register_date(self):
        return self.register_date

    def set_register_date(self, register_date):
        self.register_date = register_date
