from Model.moodModel import MoodModel
from View.view import View

class moodController:
    def _init_(self, model: MoodModel, view: View):
        self.model = model
        self.view = view