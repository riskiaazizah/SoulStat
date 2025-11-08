from Model.moodModel import MoodModel
from View.view import View

class MoodController:
    def _init_(self, model: MoodModel, view: View):
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