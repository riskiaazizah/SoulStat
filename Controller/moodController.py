from Model.moodModel import MoodModel
from View.view import View

class MoodController:
    def __init__(self, model: MoodModel, view: View):
        self.model = model
        self.view = view
        
    def tambahMood(self):
        mood = self.view.tanyaMood()
        tanggal = self.model.add_mood(mood)
        rekom = self.model.getRekomendasi(mood)
        self.view.tampilanRekomendasi(mood, rekom)

    def tampilkanRekomendasi(self):
        mood = self.view.tanyaMood()
        rekom = self.model.getRekomendasi(mood)
        self.view.tampilanRekomendasi(mood, rekom)

    def hapusMood(self):
        data = self.model.getSemuaMood()
        self.view.tabelTampilanMood(data)
        if not data:
            return
        try:
            index = int(input("Masukkan nomor yang ingin dihapus: ")) - 1
            deleted = self.model.hapusMood(index)
            self.view.konfirmasiTerhapus(deleted)
        except ValueError:
            self.view.tampilkanError("Input harus berupa angka.")
    
    def hitungKebahagiaan(self, score):
        score = self.model.getNilaiMood()
        self.view.tampilanNilaiKebahagiaan(score)
        
    def tampilkanRiwayat(self):
        data = self.model.getSemuaMood()
        self.view.tabelTampilanMood(data)

    def tampilkanStatistik(self):
        stats = self.model.getStatistik()
        self.view.tampilanStatistik(stats)

    def tampilkanQuote(self):
        quote = self.model.getQuote()
        self.view.tampilanPengingat(quote)

    def tampilkanPengingat(self):
        reminder = self.model.getPengingat()
        self.view.tampilanPengingat(reminder)
