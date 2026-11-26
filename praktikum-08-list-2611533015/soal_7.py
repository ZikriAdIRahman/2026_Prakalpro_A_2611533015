# Name : Zikri Adi Rahman
# NIM : 2611533015
# Question 7

menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

for day in range(1, number_of_days + 1):
    day_sales = []
    for menu in menus:
        portion = int(input(f"Day {day}, {menu}: "))
        day_sales.append(portion)
    sales.append(day_sales)

print("Total per day:")
for i in range(len(sales)):
    day_total = 0
    for j in range(len(sales[i])):
        day_total += sales[i][j]
    print(f"Day {i + 1}: {day_total}")

total_menu = []
for j in range(len(menus)):
    menu_total = 0
    for i in range(len(sales)):
        menu_total += sales[i][j]
    total_menu.append((menus[j], menu_total))

print("Total per menu:", total_menu)

best_name = total_menu[0][0]
best_total = total_menu[0][1]

for name, total in total_menu:
    if total > best_total:
        best_total = total
        best_name = name

print(f"Best seller: {best_name} ({best_total})")