

class User:
    def __init__(self, username, e_mail, password, register_date):
        self.username = username
        self.e_mail = e_mail
        self.password = password
        self.register_date = register_date

    def __str__(self):
        return f"""User
Username: {self.username}
E-Mail: {self.e_mail}
Passwort: {self.password}
Registrierungsdatum: {self.register_date}"""

    def get_username(self):
        return self.username

    def get_e_mail(self):
        return self.e_mail

    def get_password(self):
        return self.password

    def get_register_date(self):
        return self.register_date
