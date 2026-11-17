print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_3015 = input("Masukkan Nama Mahasiswa : ")
kelamin_3015 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3015 = int(input("Masukkan Umur : "))
skor_3015 = float(input("Masukkan Skor Tes Awal : "))

alamat_3015 = """
Parak Gadang Ganting,
Kecamatan Padang Timur,
Kota Padang,
Sumatera Barat,
Indonesia
"""
from typing import Final
kkm_3015: Final = 75.0
token_3015 = 100+3j
lulus_3015 = skor_3015 > kkm_3015

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ",nama_3015," | ",type(nama_3015))
print("Jenis Kelamin : ",kelamin_3015," | ",type(kelamin_3015))
print("Alamat Domisili : ",alamat_3015," | ",type(alamat_3015))
print("Umur : ",umur_3015," tahun | ",type(umur_3015))
print("Skor Tes Awal : ",skor_3015," | ",type(skor_3015))
print("ID Token Sinyal: ",token_3015," | ",type(token_3015))

print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai: ",kkm_3015," | ",type(kkm_3015))
print("Apakah Dinyatakan Lulus?: ",lulus_3015," | ",type(lulus_3015))