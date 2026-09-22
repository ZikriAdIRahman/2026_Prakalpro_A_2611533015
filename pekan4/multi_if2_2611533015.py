# Buat file dengan nama multi_if2_2611533015.py
# Buat program untuk kondisional If
# Nama variabel ditambah 4 digit nim terakhir contoh ipk_1234
# Program ini menggunakan fungsi input()
# Program Menghitung Diskon belanja

# Input dari user
total_belanja_3015 = float(input("Input Total Belanja (Rp): "))

# Input status member
input_member_3015 = input("Apakah Anda Member (y/t): ").strip().lower()
is_member_3015 = input_member_3015 in ["y", "ya"]

#Input status kode promo
input_promo_3015 = input("Apakah Kode Promo valid (y/t): ").strip().lower()
kode_promo_valid_3015 = input_promo_3015 in ["y", "ya"]

total_diskon_persen_3015 = 0

# MULTI-IF terpisah Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk jika memenuhi beberapa syarat sekaligus

if total_belanja_3015 >= 1000000:
    total_diskon_persen_3015 += 10  # Diskon 10% untuk belanja >= 1 juta

if is_member_3015:
    total_diskon_persen_3015 += 5  # Diskon tambahan 5% untuk member

if kode_promo_valid_3015:
    total_diskon_persen_3015 += 15  # Diskon tambahan 15% untuk kode promo valid

# Menghitung nominal diskon dan total bayar
nominal_diskon_3015 = (total_diskon_persen_3015 / 100) * total_belanja_3015
total_bayar_3015 = total_belanja_3015 - nominal_diskon_3015

# Output hasil perhitungan diskon
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_3015}% (Rp {nominal_diskon_3015:.0f})")
print(f"Total Bayar   : Rp {total_bayar_3015:.0f}")

print(f"Total Diskon yang anda dapatkan : {total_diskon_persen_3015}%")
#Output: Total diskon yang anda dapatkan : 30% jika belanja > 1 juta, member, dan kode promo valid