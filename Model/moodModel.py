import datetime
import random

class moodModel:
    def _init_(self):
        self.data_mood = []

    def add_mood(self, mood):
        tanggal = datetime.date.today().strftime("%Y-%m-%d")
        self.data_mood.append({"tanggal": tanggal, "mood": mood})
        return tanggal

    def get_all_moods(self):
        return self.data_mood