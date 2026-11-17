# Buar file dengan nama Boolean_2611533015
# Nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan tipe data Boolean
is_lulus_3015 = True
is_cumlaude_3015 = True

# Menggunakan Boolean
nilai_3015 = 85
batas_lulus_3015 = 75

# Menantukan nilai Boolean dari kondisi
status_kelulusan_3015 = nilai_3015 >= batas_lulus_3015 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai: ",nilai_3015)
print("Apakah lulus?: ",status_kelulusan_3015)
if is_lulus_3015 and is_cumlaude_3015:
    print("Selamat, Anda lulus dengan predikat Cum Laude!")