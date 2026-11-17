print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_3015 = int(input("Masukkan ukuran skala jam pasir (N): "))

# ---------- Bingkai atas ----------
print("#", end="")
for kolom_3015 in range(4 * n_3015 + 5):
    print("=", end="")
print("#", end="")
print()

# ---------- Fase 1: Jam pasir atas (baris N turun s.d. 1) ----------
for baris_3015 in range(n_3015, 0, -1):
    print("| ", end="")
    for spasi_3015 in range(2 * (n_3015 - baris_3015)):
        print(" ", end="")
    for angka_3015 in range(baris_3015, 0, -1):
        print(angka_3015, end=" ")
    print("<*>", end="")
    for angka_3015 in range(1, baris_3015 + 1):
        print(" ", end="")
        print(angka_3015, end="")
    for spasi_3015 in range(2 * (n_3015 - baris_3015)):
        print(" ", end="")
    print(" |", end="")
    print()

# ---------- Fase 2: Poros titik pusat ----------
print("|", end="")
for spasi_3015 in range(2 * n_3015 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_3015 in range(2 * n_3015 + 1):
    print(" ", end="")
print("|", end="")
print()

# ---------- Fase 3: Jam pasir bawah (baris 1 naik s.d. N) ----------
for baris_3015 in range(1, n_3015 + 1):
    print("| ", end="")
    for spasi_3015 in range(2 * (n_3015 - baris_3015)):
        print(" ", end="")
    for angka_3015 in range(baris_3015, 0, -1):
        print(angka_3015, end=" ")
    print("<*>", end="")
    for angka_3015 in range(1, baris_3015 + 1):
        print(" ", end="")
        print(angka_3015, end="")
    for spasi_3015 in range(2 * (n_3015 - baris_3015)):
        print(" ", end="")
    print(" |", end="")
    print()

# ---------- Bingkai bawah ----------
print("#", end="")
for kolom_3015 in range(4 * n_3015 + 5):
    print("=", end="")
print("#", end="")
print()