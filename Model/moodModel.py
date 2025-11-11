import datetime
import random

class MoodModel:
    def __init__(self):
        self.data_mood = []

    def add_mood(self, mood):
        tanggal = datetime.date.today().strftime("%Y-%m-%d")
        self.data_mood.append({"tanggal": tanggal, "mood": mood})
        return tanggal

    def getSemuaMood(self):
        return self.data_mood
    
    def getRekomendasi(self, mood):
        rekom = {
            "Senang": "Nice! Sistem emosimu lagi stable ✅. Share good vibes-nya sebelum expired! 🌞",
            "Sedih": "Error detected: low dopamine levels 😢. Fix it with comfort food or cute cat videos 🐱💖",
            "Stres": "CPU overheating detected 🧠💨. Time to cool down—breathe, stretch, maybe touch some grass 🌿",
            "Netral": "System idle mode ☕. Maybe spice it up a bit—listen to your favorite playlist or dance randomly 💃"
        }
        return rekom.get(mood, "Tetap semangat hari ini!")
    
    def getNilaiMood(self):
        skor_map = {"Senang": 4, "Netral": 3, "Sedih": 2, "Stres": 1}
        if not self.data_mood:
            return 0
        total = sum(skor_map[m["mood"]] for m in self.data_mood)
        return total / len(self.data_mood)
    
    def hapusMood(self, index):
        if 0 <= index < len(self.data_mood):
            return self.data_mood.pop(index)
        return None
    
    def getStatistik(self):
        stats = {"Senang": 0, "Sedih": 0, "Stres": 0, "Netral": 0}
        for item in self.data_mood:
            stats[item["mood"]] += 1
        return stats
    
    def getQuote(self):
        quotes = [
            "You're stronger better than you think 💪",
            "Bad days are just pages in your story 🌈",
            "Be kind to yourself today 🌻",
            "Small steps in everyday lead to big change in the future 🚀",
            "Life’s like coffee without sugar—just enough flavor, no drama.",
            "Sometimes life’s just like a movie with no plot twists—no surprises, just chill.",
            "I'm stronger than I've been before.",
            "In the end, you gonna be alright.",
            "Cause you still the same but only entirely diferent"
        ]
        return random.choice(quotes)
    
    def getPengingat(self):
        reminders = [
        "Minum air sekarang juga 💧",
        "Waktunya istirahat sejenak 😌",
        "Jangan lupa tersenyum hari ini 😊",
        "Gerakkan badanmu sebentar 🧘",
        "Jangan lupa beribadah 🤲",
        "Cek postur dudukmu, jangan bungkuk 💺",
        "Tarik napas dalam dan rileks 🌿",
        "Udah makan belum? 🍽",
        "Coba stretching dulu biar nggak kaku 🙆",
        "Lihat hal-hal kecil yang bisa kamu syukuri hari ini ✨",
        "Jauhkan HP sebentar, istirahatkan matamu 👀",
        "Bersihkan meja atau ruang kerjamu 🧹",
        "Tulis hal baik yang terjadi hari ini 📝",
        "Coba senyum ke diri sendiri di cermin 😁",
        "Waktunya jalan-jalan kecil keliling rumah 🚶",
        "Jangan terlalu keras sama diri sendiri 💖",
        "Dengerin lagu favoritmu sebentar 🎧",
        "Kirim pesan ke teman atau keluarga, tanyakan kabar mereka 💬",
        "Minum air hangat biar tubuh segar lagi ☕",
        "Ingat, kamu udah berjuang sejauh ini — good job! 🌈"
        ]
        return random.choice(reminders)

