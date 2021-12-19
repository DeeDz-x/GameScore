class usk:

    def __init__(self, id, name, classification, picture):
        self.id = id
        self.name = name
        self.classification = classification
        self.picture

    def __str__(self):
        return f"""USK
            USK id: {self.id}
            Name: {self.name}
            Einstufung: {self.classification}
            Bild: {self.picture}
            """    

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getClassification(self):
        return self.classification

    def getPicture(self):
        return self.picture