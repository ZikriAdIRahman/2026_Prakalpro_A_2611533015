# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_3015 = int(input("Input angka-1: "))
angka2_3015 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_3015)
print("Nilai angka2 =", angka2_3015)

# Assignment biasa
hasil_3015 = angka1_3015
print("\nAssignment biasa (=)")
print("Hasil =", hasil_3015)

# Assignment penambahan
hasil_3015 = angka1_3015
hasil_3015 += angka2_3015
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_3015)

# Assignment pengurangan
hasil_3015 = angka1_3015
hasil_3015 -= angka2_3015
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_3015)

# Assignment perkalian
hasil_3015 = angka1_3015
hasil_3015 *= angka2_3015
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_3015)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3015 != 0:
    hasil_3015 = angka1_3015
    hasil_3015 /= angka2_3015
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_3015)

    # Operator tambahan
    hasil_3015 = angka1_3015
    hasil_3015 //= angka2_3015
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_3015)

    hasil_3015 = angka1_3015
    hasil_3015 %= angka2_3015
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_3015)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_3015 = angka1_3015
hasil_3015 **= angka2_3015
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_3015)