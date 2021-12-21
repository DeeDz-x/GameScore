class Usk:

    def __init__(self, id, name, classification, picture):
        self.id = id
        self.name = name
        self.classification = classification
        self.picture = picture

    def __str__(self):
        return f"""USK
            USK id: {self.id}
            Name: {self.name}
            Einstufung: {self.classification}
            Bild: {self.picture}
            """

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_classification(self):
        return self.classification

    def get_picture(self):
        return self.picture
