class Picture:

    def __init__(self, id, path, priority, creation_date, change_date):
        self.id = id
        self.path = path
        self.priority = priority
        self.creation_date = creation_date
        self.change_date = change_date

    def __str__(self):
        return f"""Picture
            ID: {self.id}
            Pfad: {self.path}
            Beschreibung: {self.priority}
            Erstellungs Datum: {self.creation_date}
            Änderungs Datum: {self.change_date}
            """

    def get_id(self):
        return self.id

    def get_path(self):
        return self.path

    def get_priority(self):
        return self.priority

    def get_creation_date(self):
        return self.creation_date

    def get_change_date(self):
        return self.change_date
