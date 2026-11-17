# Buat File dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam python
# Nama variabale di tambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_3015 = int(input("Input angka-1: "))
angka2_3015 = int(input("Input angka-2: "))

# Penjumlahan
hasil_3015 = angka1_3015 + angka2_3015
print("\nOperator Penjumlahan")
print("Hasil =", hasil_3015)

# Pengurangan
hasil_3015 = angka1_3015 - angka2_3015
print("\nOperator Pengurangan")
print("Hasil =", hasil_3015)

# Perkalian
hasil_3015 = angka1_3015 * angka2_3015
print("\nOperator Perkalian")
print("Hasil =", hasil_3015)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_3015 != 0:
    hasil_3015 = angka1_3015 / angka2_3015
    print("\nOperator Pembagian")
    print("Hasil =", hasil_3015)

    hasil_3015 = angka1_3015 // angka2_3015
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_3015)

    hasil_3015 = angka1_3015 % angka2_3015
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_3015)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_3015 = angka1_3015 ** angka2_3015
print("\nOperator Pangkat")
print("Hasil =", hasil_3015)