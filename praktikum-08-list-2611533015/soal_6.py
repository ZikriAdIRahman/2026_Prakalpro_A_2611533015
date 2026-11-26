# Name : Zikri Adi Rahman
# NIM : 2611533015
# Question 6

LAST_DIGIT = 5  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below

for i in range(1, 8):
    expense = int(input(f"Day {i}: "))
    expenses.append(expense)

total = 0
highest = expenses[0]
highest_day = 1
above_limit = 0

for i in range(len(expenses)):
    total += expenses[i]

    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1

    if expenses[i] > daily_limit:
        above_limit += 1

average = total / len(expenses)

print("Daily limit:", daily_limit)
print("Total:", total)
print("Average:", round(average, 1))
print("Highest: day", highest_day, f"({highest})")
print("Days above limit:", above_limit)