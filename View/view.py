class View:
    def tampilkanMenu(self):
        print("\n===============================")
        print("  👋 Welcome to SoulStat 👋")
        print("===============================")
        print("1. Input Mood Harian")
        print("2. Lihat Rekomendasi Aktivitas")
        print("3. Quotes Harian")
        print("4. Skor Kebahagiaan")
        print("5. Lihat Riwayat Mood")
        print("6. Statistik Mood")
        print("7. Hapus Data Mood")
        print("8. Pengingat Harian")
        print("0. Keluar")
        print("===============================")
        return input("Pilih menu (0–8): ")
    
    def tabelTampilanMood(self, data):
        if not data:
            print("\n📭 Belum ada data mood tersimpan.")
            return
        print("\n===============================")
        print("📅 Riwayat Mood")
        print("===============================")
        print("No | Tanggal      | Mood")
        print("---------------------------------")
        for i, item in enumerate(data, start=1):
            print(f"{i:<2} | {item['tanggal']} | {item['mood']}")
        print("---------------------------------")

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

    def tampilkanError(self, message):
        print(f"\n⚠️ {message}")

    def konfirmasiTerhapus(self, deleted):
        if deleted:
            print(f"\n✅ Data tanggal {deleted['tanggal']} berhasil dihapus!")
        else:
            print("\n❌ Nomor tidak valid.")
    
    def tampilanNilaiKebahagiaan(self, score):
        print(f"\n🌈 Skor kebahagiaan kamu: {score:.2f} / 4")

    def tabelTampilanMood(self, data):
        if not data:
            print("\n📭 Belum ada data mood tersimpan.")
            return
        print("\n===============================")
        print("📅 Riwayat Mood")
        print("===============================")
        print("No | Tanggal      | Mood")
        print("---------------------------------")
        for i, item in enumerate(data, start=1):
            print(f"{i:<2} | {item['tanggal']} | {item['mood']}")
        print("---------------------------------")

    def tampilanStatistik(self, stats):
        print("\n📈 Statistik Mood Mingguan")
        print("---------------------------------")
        for mood, count in stats.items():
            print(f"{mood:<8}: {count} hari")
        print("---------------------------------")

    def tampilanPengingat(self, reminder):
        print(f"\n🔔 Reminder: {reminder}")

