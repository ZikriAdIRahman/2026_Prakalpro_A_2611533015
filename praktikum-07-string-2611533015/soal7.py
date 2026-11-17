# Name : Zikri Adi Rahman
# NIM : 2611533015
# Question 7

name = "Putri Anggraini"
nim = "2610518476"

username = name.strip().split()[0].lower() + nim[-3:]
angkatan = "20" + nim[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {angkatan}")
print("=" * 30)