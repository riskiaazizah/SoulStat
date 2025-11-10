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
                controller.tampilkanQuote()
            case "4" :
                controller.hitungKebahagiaan()
            case "5" :
                controller.tampilkanRiwayat()
            case "6" :
                controller.tampilkanStatistik()
            case "7" :
                controller.hapusMood()
            case "8" :
                controller.tampilkanPengingat()
            case "0":
                print("\n👋 Terima kasih telah menggunakan SoulStat!")
                exit()

if __name__ == "__main__":
    main()
