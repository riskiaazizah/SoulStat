from Model.moodModel import MoodModel
from View.view import View

class moodController:
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