# Sistem Loket Terpadu & Audit Transaksi Ekspedisi Wahana
# Disusun murni menggunakan pilar percabangan Pekan 4:
#   1. if tunggal           -> validasi kelogisan kuota tiket
#   2. if-elif-else         -> validasi izin kendali wahana (operator logika and, !=)
#   3. match-case (1-5, _)  -> pemilihan paket wahana
#   4. multi-if terpisah    -> akumulasi diskon bertingkat (diskon ditumpuk)
#   5. if-else              -> evaluasi kelulusan audit (bonus souvenir)
# Tidak ada nested-if (if di dalam if).
# Nama variabel WAJIB diakhiri 4 digit NIM terakhir (_3015), format snake_case.

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# ============ 1. INPUT DATA PENGUNJUNG & STRING HANDLING ============
nama_3015 = input("Masukkan Nama Pengunjung        : ")
umur_3015 = int(input("Input umur anda                 : "))
sim_3015 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()[0]

# Menu paket wahana
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_3015 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_3015 = int(input("Masukkan jumlah tiket           : "))

# ---- IF TUNGGAL: validasi kelogisan kuota tiket ----
if jumlah_tiket_3015 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")

is_member_3015 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_valid_3015 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# ============ 2. PEMILIHAN WAHANA MENGGUNAKAN MATCH-CASE (1-5 DAN _) ============
match paket_3015:
    case 1:
        nama_paket_3015 = "Wahana Safari Rimba"
        harga_satuan_3015 = 50000
    case 2:
        nama_paket_3015 = "Wahana Arung Jeram"
        harga_satuan_3015 = 75000
    case 3:
        nama_paket_3015 = "Wahana Motor ATV Ekstrim"
        harga_satuan_3015 = 120000
    case 4:
        nama_paket_3015 = "Wahana Roller Coaster Kilat"
        harga_satuan_3015 = 100000
    case 5:
        nama_paket_3015 = "Wahana All-Access VIP"
        harga_satuan_3015 = 220000
    case _:
        print("Paket wahana tidak valid!")
        exit()

# ============ 3. VALIDASI IZIN KENDALI WAHANA (IF-ELIF-ELSE + and / !=) ============
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
# Rantai if-elif-else tunggal tanpa nested-if.
# Untuk paket 3 (Motor ATV Ekstrim) evaluasi izin pengendara,
# sedangkan untuk paket selain 3 cukup cek umur >= 10 tahun.
if paket_3015 == 3 and umur_3015 >= 17 and sim_3015 == "y":
    print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
elif paket_3015 == 3 and umur_3015 >= 17 and sim_3015 != "y":
    print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
elif paket_3015 == 3 and umur_3015 < 17 and sim_3015 == "y":
    print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
elif paket_3015 == 3:
    print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
elif umur_3015 >= 10:
    print(f"Status Akses: Umur memenuhi syarat (>= 10 tahun). {nama_3015} dipersilakan menikmati {nama_paket_3015}.")
else:
    print("Status Akses: Maaf, umur belum mencukupi (minimal 10 tahun) untuk wahana ini.")

# ============ 4. AKUMULASI DISKON BERTINGKAT (MULTI-IF TERPISAH) ============
subtotal_3015 = harga_satuan_3015 * jumlah_tiket_3015
total_diskon_persen_3015 = 0

# Setiap blok if independen (bukan elif) sehingga diskon dapat diakumulasikan/ditumpuk.
if subtotal_3015 >= 200000:
    total_diskon_persen_3015 += 10  # Diskon Belanja Besar

if is_member_3015 in ["y", "ya"]:
    total_diskon_persen_3015 += 5  # Diskon Member

if kode_promo_valid_3015 in ["y", "ya"]:
    total_diskon_persen_3015 += 15  # Diskon Voucher Promo

if jumlah_tiket_3015 >= 5:
    total_diskon_persen_3015 += 5  # Diskon Tambahan Rombongan

# ============ 5. EVALUASI KELULUSAN AUDIT (IF-ELSE) ============
nominal_diskon_3015 = subtotal_3015 * (total_diskon_persen_3015 / 100)
total_bayar_3015 = subtotal_3015 - nominal_diskon_3015

print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_3015:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_3015}% (Rp {nominal_diskon_3015:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_3015:,.0f}")

if total_bayar_3015 > 300000:
    print("Catatan Layanan  : Selamat! Anda berhak mendapatkan Souvenir Gratis.")
else:
    print("Catatan Layanan  : Terima kasih telah berkunjung.")

print("Program Selesai")