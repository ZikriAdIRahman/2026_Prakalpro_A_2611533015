# Buat file dengan nama Konstanta_2611533015
# Program ini menggunakan konstanta untuk menghitun luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_3015

from typing import Final
PI: Final = 3.14
print("Pi: %f" % (PI))
jari_3015 = float(input("Masukkan nilai jari-jari: "))
luas_3015 = PI * jari_3015
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3015,luas_3015))