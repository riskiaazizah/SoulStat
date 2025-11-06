from Model.moodModel import MoodModel
from View.cli_view import CLIView

class moodController:
    def _init_(self, model: MoodModel, view: CLIView):
        self.model = model
        self.view = view