class game:

    def __init__(self, name, release, description, website, 
            creationDate, changeDate, publisher, usk, picture, genre, game = []):
        self.name = name
        self.release = release
        self.description = description
        self.website = website
        self.creationDate = creationDate
        self.changeDate = changeDate
        self.publisher = publisher
        self.usk = usk
        self.picture = picture
        self.genre = genre
        self.game = game

    def __str__(self):
        return f"""Game
            Name: {self.name}
            Veröffintlichungs Datum: {self.release}
            Beschreibung: {self.description}
            Website: {self.website}
            Erstellungs Datum: {self.creationDate}
            Änderungs Datum: {self.changeDate}
            Publisher: {self.publisher}
            USK: {self.usk}
            Bild: {self.picture}
            Genre: {self.genre}
            DLC: {self.game}
            """    

    def getId(self):
        return self.name

    def getrelease(self):
        return self.release

    def getDescription(self):
        return self.description

    def getWebsite(self):
        return self.website

    def getCreationDate(self):
        return self.creationDate

    def getChangeDate(self):
        return self.changeDate

    def getPublisher(self):
        return self.publisher

    def getUsk(self):
        return self.usk
    
    def getPicture(self):
        return self.picture
    
    def getGenre(self):
        return self.genre

    def getDlc(self)
        return self.game