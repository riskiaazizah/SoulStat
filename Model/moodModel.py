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
    
    def getRekomendasi(self, mood):
        rekom = {
            "Senang": "Pertahankan semangatmu dan sebarkan energi positif! 🌞",
            "Sedih": "Luangkan waktu untuk menenangkan diri. Dengarkan musik lembut 🎧",
            "Stres": "Coba tarik napas dalam dan istirahat sejenak 🌿",
            "Netral": "Lakukan aktivitas kecil yang menyenangkan ☕"
        }
        return rekom.get(mood, "Tetap semangat hari ini!")
    
    def hapusMood(self, index):
        if 0 <= index < len(self.data_mood):
            return self.data_mood.pop(index)
        return None
    