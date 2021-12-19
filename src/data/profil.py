

class Profil:
    def __init__(self, login_status, age, contry, name, bio, user=None):
        self.login_status = login_status
        self.age = age
        self.contry = contry
        self.name = name
        self.bio = bio
        self.user = user

    def __str__(self):
        return f"""Profil
Login Status: {self.login_status}
Alter: {self.age}
Land: {self.contry}
Name: {self.name}
Bio: {self.bio}
User: {str(self.user)}"""

    def get_login_status(self):
        return self.login_status

    def get_age(self):
        return self.age

    def get_contry(self):
        return self.contry

    def get_name(self):
        return self.name

    def get_bio(self):
        return self.bio

    def get_user(self):
        return self.user
