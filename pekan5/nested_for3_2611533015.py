# Buat file dengan nama nested_for3_NIM_py
# Buat program untuk perulangan for dalam python
# Nama variable ditabah 4 digit nim terakhir contoh: ulang_1234
# program ini menggunakan fungsi input()

batas_3015 = int(input("Masukkan Nilai Batas: "))
for i in range(1, batas_3015+1):
    for j in range(batas_3015 + 1):
        print(j+i, end=" ")
    print() # pindah ke baris berikutnya