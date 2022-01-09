from data.picture import Picture


class Publisher:

    def __init__(self, id: int, name: str, description: str, website: str, picture: Picture = None):
        self.id = id
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

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_website(self):
        return self.website

    def get_picture(self):
        return self.picture
