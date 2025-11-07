class View:
    def show_menu(self):
        print("\n===============================")
        print("🌤️  MOOD MANAGER SYSTEM")
        print("===============================")
        print("1. Input Mood Harian")
        print("2. Lihat Rekomendasi Aktivitas")
        print("3. Quotes Harian")
        print("4. Skor Kebahagiaan")
        print("5. Lihat Riwayat Mood")
        print("6. Statistik & Tren Mood")
        print("7. Hapus Data Mood")
        print("8. Reminder Harian")
        print("0. Keluar")
        print("===============================")
        return input("Pilih menu (0–8): ")
    
    def tanyaMood(self):
        print("\nPilih mood kamu hari ini:")
        print("1. Senang 😊")
        print("2. Sedih 😢")
        print("3. Stres 😣")
        print("4. Netral 😐")
        pilihan = input("Masukkan pilihan (1–4): ")
        mood_dict = {"1": "Senang", "2": "Sedih", "3": "Stres", "4": "Netral"}
        return mood_dict.get(pilihan, "Netral")

    def tampilanRekomendasi(self, mood, rekom):
        print(f"\n📊 Mood kamu hari ini: {mood}")
        print(f"💡 Rekomendasi aktivitas: {rekom}")