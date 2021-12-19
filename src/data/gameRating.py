class gameRating:

    def __init__(self, id, name, min, max, step, creationDate, changeDate):
        self.id = id
        self.name = name
        self.min = min
        self.max = max
        self.step = step
        self.creationDate = creationDate
        self.changeDate = changeDate

    def __str__(self):
        return f"""Game Rating
            Spiele Wertung ID: {self.id}
            Name: {self.name}
            Min Bewertung: {self.min}
            Max Bewertung: {self.max}
            Erhöhung: {self.step}
            Erstellungs Datum: {self.creationDate}
            Änderungs Datum: {self.changeDate}
            """    

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getMin(self):
        return self.min

    def getMax(self):
        return self.max

    def getStep(self):
        return self.step

    def getcreationDate(self):
        return self.creationDate

    def getChangeDate(self):
        return self.changeDate
    