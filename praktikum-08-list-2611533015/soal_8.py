# Name : Zikri Adi Rahman
# NIM : 2611533015
# Question 8

number_of_rows = 4
seats_per_row = 5
# Write your code below

cinema = []
for i in range(number_of_rows):
    row_list = []
    for j in range(seats_per_row):
        row_list.append(".")
    cinema.append(row_list)

while True:
    for i in range(len(cinema)):
        print(f"Row {i + 1}:", end=" ")
        for j in range(len(cinema[i])):
            print(cinema[i][j], end=" ")
        print()

    row = int(input("Row (0 to stop): "))
    if row == 0:
        break

    seat = int(input("Seat: "))

    if row < 1 or row > number_of_rows or seat < 1 or seat > seats_per_row:
        print("Invalid seat.")
    elif cinema[row - 1][seat - 1] == "X":
        print("Seat already taken.")
    else:
        cinema[row - 1][seat - 1] = "X"
        print("Seat booked.")

seats_taken = 0
for i in range(len(cinema)):
    for j in range(len(cinema[i])):
        if cinema[i][j] == "X":
            seats_taken += 1

print("Seats taken:", seats_taken)