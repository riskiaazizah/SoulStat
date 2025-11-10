from Model.moodModel import MoodModel
from View.view import View
from Controller.moodController import MoodController

def main():
    model = MoodModel()
    view = View()
    controller = MoodController(model, view)
    
    while True :
        pilihan = view.tampilkanMenu()
        
        match pilihan :
            case "1" :
                controller.tambahMood()
            case "2" :
                controller.tampilkanRekomendasi()
            case "3" :
                pass
            case "4" :
                controller.hitungKebahagiaan()
            case "5" :
                pass
            case "6" :
                pass
            case "7" :
                controller.hapusMood()
            case "0":
                print("\n👋 Terima kasih telah menggunakan SoulStat!")
                exit()

if __name__ == "__main__":
    main()
