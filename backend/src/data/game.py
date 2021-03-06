from datetime import datetime
from datetime import date
from typing import List
from data.genre import Genre
from data.picture import Picture
from data.publisher import Publisher
from data.review import Review
from data.usk import Usk


class Game:

    def __init__(self, id: int, name: str, release: str, description: str, website: str,
                 creation_date: datetime, change_date: datetime, publisher: Publisher = None,
                 usk: Usk = None, picture: List[Picture] = None, genre: Genre = None, game: List = None, review: List[Review] = None):
        self.id = id
        self.name = name
        self.release = release
        self.description = description
        self.website = website
        self.creation_date = creation_date
        self.change_date = change_date
        self.publisher = publisher
        self.usk = usk
        self.picture = picture
        self.genre = genre
        self.game = game
        if review is None:
            self.review = []
        else:
            self.review = review

    def __str__(self):
        return f"""Game
            Name: {self.name}
            Veröffintlichungs Datum: {self.release}
            Beschreibung: {self.description}
            Website: {self.website}
            Erstellungs Datum: {self.creation_date}
            Änderungs Datum: {self.change_date}
            Publisher: {self.publisher}
            USK: {self.usk}
            Bild: {self.picture}
            Genre: {self.genre}
            DLC: {self.game}
            Reviews: {self.review}
            """

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_release(self):
        return self.release

    def get_description(self):
        return self.description

    def get_website(self):
        return self.website

    def get_creation_date(self):
        return self.creation_date

    def get_change_date(self):
        return self.change_date

    def get_publisher(self):
        return self.publisher

    def get_usk(self):
        return self.usk

    def get_picture(self):
        return self.picture

    def get_genre(self):
        return self.genre

    def get_dlc(self):
        return self.game
    
    def get_review(self):
        return self.review
    
    def add_review(self,review:Review):
        self.review.append(review)
