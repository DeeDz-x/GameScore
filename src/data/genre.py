class genre:

    def __init__(self, id, name, description, creationDate):
        self.id = id
        self.name = name
        self.description = description
        self.creationDate = creationDate

    def __str__(self):
        return f"""Genre
            ID: {self.id}
            Genre: {self.name}
            Beschreibung: {self.description}
            Erstellungs Datum: {self.creationDate}
            """    

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getcreationDate(self):
        return self.creationDate