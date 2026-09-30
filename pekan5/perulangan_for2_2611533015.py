# Buat file dengan nama perulangan_for2_NIM_py
# Buat program untuk perulangan for dalam python
# Nama variable ditabah 4 digit nim terakhir contoh: ulang_1234
# program ini menggunakan fungsi input()

ulang_3015 = int(input("Masukkan Jumblah Perulangan: "))
print ("Perulangan ke-0 sampai ke-", ulang_3015-1)
for i in range(ulang_3015):
    print(i, end=" ")
print()
print("Perulangan ke-1 sampai ke-", ulang_3015)
for i in range(1,ulang_3015+1):
    print(i, end=" ")
