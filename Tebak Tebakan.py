import random
from dataset import dataset # Dataset lokal berisi pertanyaan dan jawaban geografi

# Fungsi untuk mendapatkan pertanyaan secara acak
def ambil_pertanyaan_acak():
    
    return random.choice(dataset) #  Mengambil satu pertanyaan secara acak dari dataset.

# Fungsi untuk memeriksa jawaban
def periksa_jawaban(jawaban_user, jawaban_benar):
    """
    Membandingkan jawaban user dengan jawaban yang benar.
    """

    if jawaban_user.strip().lower() == jawaban_benar.strip().lower():
        return "Benar!"
    else:
        return f"Salah! Jawabannya: {jawaban_benar}"

# DI MULAI NYA DI SINI
if __name__ == "__main__":
    print("Selamat datang di Tebak-Tebakan Geografi!")
    while True:
        try:
            # Mengambil pertanyaan secara acak
            data_pertanyaan = ambil_pertanyaan_acak()
            pertanyaan = data_pertanyaan["question"]
            jawaban_benar = data_pertanyaan["answer"]

            # Menampilkan pertanyaan ke user
            print(f"\nPertanyaan: {pertanyaan}")
            jawaban_user = input("Jawaban Anda: ")

            # Memeriksa jawaban user
            umpan_balik = periksa_jawaban(jawaban_user, jawaban_benar)
            print(umpan_balik)

            # Menanyakan apakah user ingin melanjutkan permainan
            lanjut = input("Ingin lanjut? (y/n): ").strip().lower()
            if lanjut != 'y':
                print("Terima kasih telah bermain!")
                break

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            break
