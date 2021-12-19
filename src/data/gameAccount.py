class gameAccount:

    def __init__(self, id, typ, profile, changeDate):
        self.id = id
        self.typ = typ
        self.profile = profile
        self.changeDate = changeDate

    def __str__(self):
        return f"""Game Account
            Spieleacount id: {self.id}
            Platform: {self.typ}
            Profil: {self.profile}
            Änderungs Datum: {self.changeDate}
            """    

    def getId(self):
        return self.id

    def getTyp(self):
        return self.typ

    def getProfile(self):
        return self.profile

    def getChangeDate(self):
        return self.changeDate
    