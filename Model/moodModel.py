import datetime
import random

class moodModel:
    def delete_mood(self, index):
        if 0 <= index < len(self.data_mood):
            return self.data_mood.pop(index)
        return None
