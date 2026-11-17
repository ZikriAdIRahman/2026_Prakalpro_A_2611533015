# Name : Zikri Adi Rahman
# NIM : 2611533015
# bonus

kalimat = input("Masukkan kalimat: ")
teks = kalimat.replace(" ", "").lower()

if teks == teks[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")