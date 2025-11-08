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
            "Senang": "Nice! Sistem emosimu lagi stable ✅. Share good vibes-nya sebelum expired! 🌞",
            "Sedih": "Error detected: low dopamine levels 😢. Fix it with comfort food or cute cat videos 🐱💖",
            "Stres": "CPU overheating detected 🧠💨. Time to cool down—breathe, stretch, maybe touch some grass 🌿",
            "Netral": "System idle mode ☕. Maybe spice it up a bit—listen to your favorite playlist or dance randomly 💃"
        }
        return rekom.get(mood, "Tetap semangat hari ini!")
    
    def hapusMood(self, index):
        if 0 <= index < len(self.data_mood):
            return self.data_mood.pop(index)
        return None
    