from Model.moodModel import MoodModel
from View.view import View
from Controller.moodController import MoodController

def main():
    model = MoodModel()
    view = View()
    controller = MoodController(model, view)
    
    while True :
        pilihan = view.show_menu()
        
        match pilihan :
            case "1" :
                controller.tambahMood()
            
            case "2" :
                controller.tampilkanRekomendasi()
            
        
                
        
        