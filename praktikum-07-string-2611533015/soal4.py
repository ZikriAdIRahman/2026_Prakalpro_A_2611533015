# Name : Zikri Adi Rahman
# NIM : 2611533015
# Question 4

phone = "087872518822"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)