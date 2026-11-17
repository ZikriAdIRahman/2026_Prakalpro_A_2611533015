# ============================================================
#  SISTEM SIMULASI TRANSAKSI DAN VALIDASI AKSES TOKO
#  Tugas Praktikum 3 - Operator Python
#  NIM 2611533015
#
#  Program kasir sederhana untuk menghitung total transaksi,
#  memvalidasi status pelanggan, dan menentukan hak akses promo.
#  Seluruh jenis operator Python terintegrasi dalam satu alur.
# ============================================================

print("=== SISTEM TRANSAKSI TOKO ===\n")

# ---------- INPUT DATA PELANGGAN ----------
nama_3015 = input("Masukkan Nama Pelanggan : ").strip()
status_3015 = input("Masukkan Status Pelanggan (member/nonmember) : ").strip().lower()
total_belanja_3015 = float(input("Masukkan Total Belanja : "))
jumlah_barang_3015 = int(input("Masukkan Jumlah Barang : "))
kode_promo_3015 = input("Masukkan Kode Promo : ").strip().upper()

# daftar promo
daftar_promo_3015 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# ---------- OPERATOR PERBANDINGAN ----------
# Memeriksa apakah syarat diskon / promo terpenuhi (hasil True/False)
minimal_belanja_3015 = total_belanja_3015 >= 200000
minimal_barang_3015 = jumlah_barang_3015 >= 3
status_member_3015 = status_3015 == "member"
bukan_member_3015 = status_3015 != "member"

# ---------- OPERATOR LOGIKA ----------
# Diskon khusus member : member AND belanja mencapai batas minimum
diskon_member_3015 = status_member_3015 and minimal_belanja_3015
# Syarat mendapat poin bonus : member OR jumlah barang minimal 3
syarat_poin_3015 = status_member_3015 or minimal_barang_3015
# Kebalikan dari status member
nonmember_3015 = not status_member_3015

# ---------- OPERATOR KEANGGOTAAN ----------
# Memeriksa apakah kode promo user terdapat dalam daftar promo
promo_tersedia_3015 = kode_promo_3015 in daftar_promo_3015
promo_tidak_ada_3015 = kode_promo_3015 not in daftar_promo_3015
# Pelanggan mendapatkan promo jika jumlah barang >= 3 DAN promo tersedia
dapat_promo_3015 = minimal_barang_3015 and promo_tersedia_3015

# ---------- OPERATOR ARITMATIKA DAN PENUGASAN ----------
# Besar diskon dihitung bertahap memakai augmented assignment (+=)
besar_diskon_3015 = 0.0                     # operator penugasan (=)
if minimal_belanja_3015:                    # 10% utk belanja >= Rp200.000
    besar_diskon_3015 += (10.0 / 100) * total_belanja_3015
if diskon_member_3015:                      # +5% khusus member
    besar_diskon_3015 += (5.0 / 100) * total_belanja_3015
if dapat_promo_3015:                        # +5% bila kode promo valid
    besar_diskon_3015 += (5.0 / 100) * total_belanja_3015

# Pelanggan dikatakan mendapat diskon bila besar diskon lebih dari 0
mendapat_diskon_3015 = besar_diskon_3015 > 0

# Total pembayaran setelah dipotong diskon (operator pengurangan)
total_bayar_3015 = total_belanja_3015       # penugasan awal
total_bayar_3015 -= besar_diskon_3015       # augmented assignment (-=)

# Harga rata-rata barang setelah diskon (operator pembagian)
if jumlah_barang_3015 > 0:
    rata_rata_barang_3015 = total_bayar_3015 / jumlah_barang_3015
else:
    rata_rata_barang_3015 = 0.0

# Sisa pembagian total belanja bila dibayar pecahan Rp10.000 (modulo %)
sisa_pembagian_3015 = int(total_belanja_3015) % 10000

# Poin loyalitas : 10 poin per Rp50.000, dikali 2 bila syarat terpenuhi
poin_3015 = 0
poin_3015 += int(total_bayar_3015 // 50000) * 10
if syarat_poin_3015:
    poin_3015 *= 2                          # augmented assignment (*=)

# ---------- OPERATOR IDENTITAS ----------
# is  -> membandingkan IDENTITAS objek (apakah menunjuk objek yang sama)
# ==  -> membandingkan NILAI/ISI objek (apakah isinya sama)
referensi_promo_3015 = daftar_promo_3015            # objek yang SAMA
salinan_promo_3015 = list(daftar_promo_3015)        # objek BARU, isi sama

identitas_sama_3015 = daftar_promo_3015 is referensi_promo_3015
identitas_beda_3015 = daftar_promo_3015 is not salinan_promo_3015
nilai_sama_3015 = daftar_promo_3015 == salinan_promo_3015

# ---------- OPERATOR BITWISE ----------
# Setiap kondisi direpresentasikan dalam bit biner :
#   0001 = member         0100 = jumlah barang >= 3
#   0010 = belanja >= 200rb   1000 = kode promo tersedia
bit_member_3015 = 0b0001 if status_member_3015 else 0
bit_belanja_3015 = 0b0010 if minimal_belanja_3015 else 0
bit_barang_3015 = 0b0100 if minimal_barang_3015 else 0
bit_promo_3015 = 0b1000 if promo_tersedia_3015 else 0

# OR (|) : menggabungkan seluruh kondisi menjadi satu kode status
kode_status_3015 = (bit_member_3015 | bit_belanja_3015 |
                    bit_barang_3015 | bit_promo_3015)

# AND (&) : memeriksa apakah suatu kondisi terpenuhi dalam kode status
cek_akses_member_3015 = kode_status_3015 & 0b0001
cek_akses_promo_3015 = kode_status_3015 & 0b1000

# Kode referensi transaksi lain : member + belanja minimal + barang minimal
kode_referensi_3015 = 0b1011

# XOR (^) : membandingkan perbedaan status antara dua kode transaksi
perbedaan_status_3015 = kode_status_3015 ^ kode_referensi_3015

# Shift kiri (<<) : menggeser kode status untuk keperluan cadangan
kode_shift_3015 = kode_status_3015 << 1

# ---------- HAK AKSES PELANGGAN ----------
hak_member_3015 = status_member_3015
hak_promo_3015 = dapat_promo_3015
hak_gratis_ongkir_3015 = kode_promo_3015 == "GRATISONGKIR"

# ================= TAMPILAN HASIL =================
print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan     : {nama_3015}")
print(f"Status Pelanggan   : {status_3015}")
print(f"Total Belanja      : Rp{total_belanja_3015:.0f}")
print(f"Jumlah Barang      : {jumlah_barang_3015}")
print(f"Kode Promo         : {kode_promo_3015}")

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200.000     : {minimal_belanja_3015}")
print(f"Jumlah Barang >= 3       : {minimal_barang_3015}")
print(f"Status Member            : {status_member_3015}")
print(f"Kode Promo Tersedia      : {promo_tersedia_3015}")
print(f"Mendapatkan Diskon       : {mendapat_diskon_3015}")
print(f"Mendapatkan Promo        : {dapat_promo_3015}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Besar Diskon             : Rp{besar_diskon_3015:.0f}")
print(f"Total Pembayaran         : Rp{total_bayar_3015:.0f}")
print(f"Rata-rata Harga Barang   : Rp{rata_rata_barang_3015:.0f}")
print(f"Sisa Pembagian (modulo)  : Rp{sisa_pembagian_3015}")
print(f"Poin Loyalitas           : {poin_3015} poin")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Member Access          : {hak_member_3015}")
print(f"Promo Access           : {hak_promo_3015}")
print(f"Free Shipping Access   : {hak_gratis_ongkir_3015}")

print("\n=== HASIL OPERATOR ===")
print("\n--- OPERATOR ARITMATIKA ---")
print(f"Total belanja                        : Rp{total_belanja_3015:.0f}")
print(f"Diskon                                : Rp{besar_diskon_3015:.0f}")
print(f"Total bayar (total belanja - diskon)  : Rp{total_bayar_3015:.0f}")
print(f"Rata-rata (total bayar / jumlah barang) : Rp{rata_rata_barang_3015:.0f}")
print(f"Modulo (total % 10000)                : {sisa_pembagian_3015}")

print("\n--- OPERATOR PERBANDINGAN ---")
print(f"{total_belanja_3015:.0f} >= 200000  -> {minimal_belanja_3015}")
print(f"{jumlah_barang_3015} >= 3         -> {minimal_barang_3015}")
print(f"status == 'member'                  -> {status_member_3015}")

print("\n--- OPERATOR LOGIKA ---")
print(f"member AND belanja_min              -> {diskon_member_3015}")
print(f"member OR  barang >= 3              -> {syarat_poin_3015}")
print(f"NOT member                          -> {nonmember_3015}")

print("\n--- OPERATOR PENUGASAN ---")
print(f"besar_diskon dihitung dengan +=     -> Rp{besar_diskon_3015:.0f}")
print(f"total_bayar dikurangi dengan -=     -> Rp{total_bayar_3015:.0f}")
print(f"poin digandakan dengan *=           -> {poin_3015} poin")

print("\n--- OPERATOR KEANGGOTAAN ---")
print(f"Daftar promo               : {daftar_promo_3015}")
print(f"'{kode_promo_3015}' in daftar      -> {promo_tersedia_3015}")
print(f"'{kode_promo_3015}' not in daftar  -> {promo_tidak_ada_3015}")

print("\n--- OPERATOR IDENTITAS ---")
print(f"daftar is referensi (objek sama)   -> {identitas_sama_3015}")
print(f"daftar is not salinan (objek baru) -> {identitas_beda_3015}")
print(f"daftar == salinan (nilai sama)     -> {nilai_sama_3015}")
print("Catatan : is membandingkan identitas objek, == membandingkan nilai/isi objek.")

print("\n--- OPERATOR BITWISE ---")
print("Format bit : 0001=member | 0010=belanja>=200rb | 0100=barang>=3 | 1000=promo")
print(f"OR (|) : {format(bit_member_3015, '04b')} | {format(bit_belanja_3015, '04b')} | {format(bit_barang_3015, '04b')} | {format(bit_promo_3015, '04b')} = {format(kode_status_3015, '04b')}")
print(f"Kode Status Transaksi   : {format(kode_status_3015, '04b')} (desimal {kode_status_3015})")
print(f"AND (&) cek member      : {format(kode_status_3015, '04b')} & 0001 = {format(cek_akses_member_3015, '04b')} ({cek_akses_member_3015})")
print(f"AND (&) cek promo       : {format(kode_status_3015, '04b')} & 1000 = {format(cek_akses_promo_3015, '04b')} ({cek_akses_promo_3015})")
print(f"XOR (^) beda status     : {format(kode_status_3015, '04b')} ^ {format(kode_referensi_3015, '04b')} = {format(perbedaan_status_3015, '04b')} ({perbedaan_status_3015})")
print(f"Shift (<<) kode         : {format(kode_status_3015, '04b')} << 1 = {format(kode_shift_3015, 'b')} ({kode_shift_3015})")

print("\n=== SELESAI ===")

