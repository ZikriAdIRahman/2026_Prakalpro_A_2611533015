# Buat file dengan nama nested_for1_NIM_py
# Buat program untuk perulangan for dalam python
# Nama variable ditabah 4 digit nim terakhir contoh: ulang_1234
# program ini menggunakan fungsi input()

batas_3015 = int(input("Masukkan Nilai Batas: "))
for line_3015 in range(1, batas_3015+1):
    for j in range(1, (-1 * line_3015 + batas_3015) + 1):
        print(" . ", end="")
    print(line_3015)