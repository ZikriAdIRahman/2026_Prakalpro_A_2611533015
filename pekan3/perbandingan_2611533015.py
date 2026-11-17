# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_3015 = int(input("Input angka-1: "))
angka2_3015 = int(input("Input angka-2: "))

# Lebih besar dari
hasil_3015 = angka1_3015 > angka2_3015
print("\nOperator lebih besar dari")
print("angka1 > angka2 =", hasil_3015)

# Lebih kecil dari
hasil_3015 = angka1_3015 < angka2_3015
print("\nOperator lebih kecil dari")
print("angka1 < angka2 =", hasil_3015)

# Lebih besar dari atau sama dengan
hasil_3015 = angka1_3015 >= angka2_3015
print("\nOperator lebih besar dari atau sama dengan")
print("angka1 >= angka2 =", hasil_3015)

# Lebih kecil dari atau sama dengan
hasil_3015 = angka1_3015 <= angka2_3015
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1 <= angka2 =", hasil_3015)

# Sama dengan
hasil_3015 = angka1_3015 == angka2_3015
print("\nOperator sama dengan")
print("angka1 == angka2 =", hasil_3015)

# Tidak sama dengan
hasil_3015 = angka1_3015 != angka2_3015
print("\nOperator tidak sama dengan")
print("angka1 != angka2 =", hasil_3015)

# Tambahan: perbandingan berantai dalam Python
hasil_3015 = 0 < angka1_3015 < 100
print("\nPerbandingan berantai")
print("0 < angka1 < 100 =", hasil_3015)

hasil_3015 = 0 < angka2_3015 < 100
print("0 < angka2 < 100 =", hasil_3015)