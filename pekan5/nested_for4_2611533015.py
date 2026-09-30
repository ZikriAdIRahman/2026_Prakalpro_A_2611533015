# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_3015 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3015 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_3015 = tinggi_3015
    c_3015 = a_3015
    lebar_3015 = (2 * tinggi_3015) - 2

    for i in range(1, tinggi_3015 + 1):
        b_3015 = c_3015 + 1

        for j in range(1, lebar_3015 + 1):

            # Baris atas dan bawah
            if i == 1 or i == tinggi_3015:
                if j == 1 or j == lebar_3015:
                    print("#", end="")
                else:
                    print("=", end="")
            # Baris isi
            else:
                if j == 1 or j == lebar_3015:
                    print("|", end="")
                else:
                    if j == c_3015:
                        print("<", end="")
                    elif j == b_3015:
                        print(">", end="")
                    elif j == (lebar_3015 - c_3015):
                        print("<", end="")
                    elif j == (lebar_3015 - c_3015 + 1):
                        print(">", end="")
                    elif j > b_3015 and j < (lebar_3015 - c_3015):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_3015 -= 2

        if a_3015 <= 0:
            c_3015 = (-a_3015) + 2
        else:
            c_3015 = a_3015