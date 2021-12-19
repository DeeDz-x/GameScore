class picture:

    def __init__(self, id, path, priority, creationDate, changeDate):
        self.id = id
        self.path = path
        self.priority = priority
        self.creationDate = creationDate
        self.changeDate = changeDate

    def __str__(self):
        return f"""Picture
            ID: {self.id}
            Pfad: {self.path}
            Beschreibung: {self.priority}
            Erstellungs Datum: {self.creationDate}
            Änderungs Datum: {self.changeDate}
            """    

    def getId(self):
        return self.id

    def getPath(self):
        return self.path

    def getPriority(self):
        return self.priority

    def getcreationDate(self):
        return self.creationDate

    def getChangeDate(self):
        return self.changeDate