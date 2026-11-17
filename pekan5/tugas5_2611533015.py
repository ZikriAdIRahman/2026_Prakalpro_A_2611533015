# Tugas output perulangan for
# Buat program untuk perulangan for dalam Python (Pola Segitiga Bintang)
# Program ini menggunakan fungsi input()

tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(1, tinggi + 1):
    # Cetak spasi di sebelah kiri agar membentuk segitiga simetris
    for j in range(tinggi - i):
        print(" ", end="")
    
    # Cetak bintang beserta spasi setelahnya
    for k in range(i):
        print("* ", end="")
    
    # Pindah ke baris baru
    print()