from Model.moodModel import MoodModel
from View.cli_view import CLIView

class moodController:
    def __init__(self, model: MoodModel, view: CLIView):
        self.model = model
        self.view = view