# Buat file dengan nama perulangan_for3_NIM_py
# Buat program untuk perulangan for dalam python
# Nama variable ditabah 4 digit nim terakhir contoh: ulang_1234
# program ini menggunakan fungsi input()

ulang_3015 = int(input("Masukkan Jumblah Perulangan: "))

jumlah_3015 = 0
for i in range(1, ulang_3015 + 1):
    print(i, end=" ")
    jumlah_3015 = jumlah_3015 + i

    if i < ulang_3015:
        print(" + ", end="")
    else:
        print(" = ", end="")
print()
print(f"jumlah = {jumlah_3015}")