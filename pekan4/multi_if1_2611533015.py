# Buat File dengan nama multi_if.py
# Buat program untuk kondisional If
# Nama variabel ditambah 4 digit nim terakhir contoh ipk_1234
# Program ini menggunakan fungsi input()

umur_3015 = int(input("Input umur Anda: "))
sim_3015 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0]

if umur_3015 >= 17 and sim_3015 == "y": 
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_3015 >= 17 and sim_3015 != "y":
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_3015 < 17 and sim_3015 != "y":
    print("Anda belum cukup umur bawa motor")

if umur_3015 < 17 and sim_3015 == "y":
    print("Anda belum cukup umur punya SIM")