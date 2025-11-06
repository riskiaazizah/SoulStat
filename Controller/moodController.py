from Model.moodModel import MoodModel
from View.cli_view import CLIView

class moodController:
    def delete_mood(self):
        data = self.model.get_all_moods()
        self.view.display_mood_table(data)
        if not data:
            return
        try:
            index = int(input("Masukkan nomor yang ingin dihapus: ")) - 1
            deleted = self.model.delete_mood(index)
            self.view.confirm_delete(deleted)
        except ValueError:
            self.view.show_error("Input harus berupa angka.")