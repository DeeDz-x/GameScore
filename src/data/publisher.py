class publisher:

    def __init__(self, name, description, website, picture):
        self.name = name
        self.description = description
        self.website = website
        self.picture = picture

    def __str__(self):
        return f"""publisher
            Publisher name: {self.name}
            Beschreibung: {self.description}
            Webseite: {self.website}
            Bilder: {self.picture}
            """    

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getWebsite(self):
        return self.website

    def getPicture(self):
        return self.picture
    
