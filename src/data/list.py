class list:

    def __init__(self, id, public, title, game):
        self.id = id
        self.public = public
        self.title = title
        self.game = game

    def __str__(self):
        return f"""List
            Listen id: {self.id}
            Öffentlich: {self.public}
            Titel: {self.title}
            Spiele: {self.game}
            """    

    def getId(self):
        return self.id

    def getPublic(self):
        return self.public

    def getTitle(self):
        return self.title

    def getGame(self):
        return self.game
    